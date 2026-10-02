"""Pure calculations and fish-generation rules for the game."""

import random
from statistics import median

from fish_data import (
    FAVOR_CHANGE_LIMIT,
    FAVOR_POINTS_PER_STEP,
    FISH_DATA,
    RARITY_BASE_VALUES,
)


def fish_for_location(location):
    """Return the catchable fish names for a location."""
    return [
        name for name, data in FISH_DATA.items()
        if location in data["locations"]
    ]


def calculate_cast_success_chance(base_chance, equipment_bonus):
    """Apply bounded gear bonuses to a cast's base success chance."""
    bounded_bonus = max(-0.10, min(0.20, equipment_bonus))
    return max(0.25, min(0.78, base_chance + bounded_bonus))


def catch_random_fish(location, active_boon=None, rng=None, fish_bonuses=None):
    """Choose a fish using location, rarity, and selected-gear weights."""
    rng = rng or random
    available = fish_for_location(location)
    fish_bonuses = fish_bonuses or {}
    weights = [
        FISH_DATA[name]["rarity_weight"] * (1 + min(1.0, fish_bonuses.get(name, 0.0)))
        for name in available
    ]

    if active_boon == "Fortune":
        rarity_multipliers = {
            "Common": 0.65,
            "Uncommon": 1.2,
            "Rare": 1.8,
            "Very Rare": 2.5,
            "Legendary": 3.5,
        }
        weights = [
            weight * rarity_multipliers[FISH_DATA[name]["rarity"]]
            for name, weight in zip(available, weights)
        ]

    return rng.choices(available, weights=weights, k=1)[0]


def calculate_fish_points(weight_kg, size_cm):
    """Score a specimen using its weight and length."""
    return round((weight_kg * 10) + size_cm, 1)


def median_fish_points(location):
    """Return the median typical score of fish at a location."""
    typical_scores = []
    for fish_name in fish_for_location(location):
        data = FISH_DATA[fish_name]
        typical_weight = sum(data["weight_kg"]) / 2
        typical_size = sum(data["size_cm"]) / 2
        typical_scores.append(
            calculate_fish_points(typical_weight, typical_size)
        )
    return median(typical_scores)


def lower_quartile_fish_points(location):
    """Return the inclusive first quartile of typical fish scores."""
    typical_scores = sorted(
        calculate_fish_points(
            sum(FISH_DATA[name]["weight_kg"]) / 2,
            sum(FISH_DATA[name]["size_cm"]) / 2,
        )
        for name in fish_for_location(location)
    )
    position = (len(typical_scores) - 1) * 0.25
    lower_index = int(position)
    upper_index = min(lower_index + 1, len(typical_scores) - 1)
    fraction = position - lower_index
    return round(
        typical_scores[lower_index]
        + (typical_scores[upper_index] - typical_scores[lower_index]) * fraction,
        1,
    )


def favor_change_for_fish(specimen):
    """Scale integer Favor changes by distance from the location median."""
    distance = abs(specimen["points"] - specimen["median_points"])
    change = int(distance // FAVOR_POINTS_PER_STEP) + 1
    return min(FAVOR_CHANGE_LIMIT, change)


def favor_loss_for_fish(specimen, active_boon=None):
    """Return Favor lost by keeping this fish."""
    if active_boon == "Fishers" or specimen["points"] == specimen["median_points"]:
        return 0

    loss = favor_change_for_fish(specimen)
    if active_boon == "Penance":
        return loss // 2
    return loss


def favor_loss_for_dump(specimen, active_boon=None):
    """Return the doubled Favor cost for discarding this fish."""
    loss = favor_change_for_fish(specimen)
    if active_boon == "Penance":
        loss //= 2
    return loss * 2


def fish_is_marketable(specimen):
    """Whether the specimen meets its catch-location market threshold."""
    return specimen["points"] >= specimen["lower_quartile_points"]


def calculate_fish_value(fish_name, weight_kg, size_cm):
    """Calculate the specimen's fixed market value in dollars."""
    rarity = FISH_DATA[fish_name]["rarity"]
    base_value = RARITY_BASE_VALUES[rarity]
    return round(base_value + (weight_kg * 0.50) + (size_cm * 0.10), 2)


def sale_payout(specimen, active_boon=None):
    """Return the price paid by the market, including Prosperity."""
    multiplier = 1.5 if active_boon == "Prosperity" else 1.0
    return round(specimen["value"] * multiplier, 2)


def generate_specimen(fish_name, location, active_boon=None, rng=None):
    """Create one unique fish specimen."""
    rng = rng or random
    data = FISH_DATA[fish_name]
    min_weight, max_weight = data["weight_kg"]
    min_size, max_size = data["size_cm"]

    if active_boon == "Giants":
        size_ratio = rng.betavariate(2, 1)
        size = min_size + (max_size - min_size) * size_ratio
    else:
        size = rng.uniform(min_size, max_size)

    expected_size_ratio = (
        (size - min_size) / (max_size - min_size)
        if max_size > min_size else 0.5
    )
    base_weight = min_weight + (
        (max_weight - min_weight) * expected_size_ratio
    )
    variation = rng.uniform(0.80, 1.20)
    weight = max(min_weight, min(max_weight, base_weight * variation))

    return {
        "name": fish_name,
        "rarity": data["rarity"],
        "weight_kg": weight,
        "size_cm": size,
        "value": calculate_fish_value(fish_name, weight, size),
        "points": calculate_fish_points(weight, size),
        "median_points": median_fish_points(location),
        "lower_quartile_points": lower_quartile_fish_points(location),
        "location": location,
    }


def format_money(amount):
    return f"${amount:,.2f}"


def format_weight(weight_kg, unit_system="imperial"):
    if unit_system == "metric":
        return f"{weight_kg:.2f} kg"
    pounds = weight_kg * 2.2046226218
    return f"{pounds:.2f} lb"


def format_size(size_cm, unit_system="imperial"):
    if unit_system == "metric":
        return f"{size_cm:.1f} cm"
    inches = size_cm / 2.54
    return f"{inches:.1f} in"
