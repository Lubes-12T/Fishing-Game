"""Mutable player and session state for one game run."""

from dataclasses import dataclass, field
import random as random_module


@dataclass
class GameState:
    player_name: str = ""
    cache: list = field(default_factory=list)
    backpack: list = field(default_factory=list)
    current_location: str = "Freshwater Lake"
    unit_system: str = "imperial"
    money: float = 0.0
    favor: int = 0
    casts_since_favor_recovery: int = 0
    owned_boons: set = field(default_factory=set)
    active_boon: str | None = None
    researched_fish: set = field(default_factory=set)
    dialogue_random: random_module.Random = field(default_factory=random_module.Random)
    random: random_module.Random = field(default_factory=random_module.Random)
    greeting_decks: dict = field(default_factory=dict)
    time_minutes: int = 6 * 60
    selected_bait: str | None = "wad"
    selected_rod: str = "Old Rod"
    selected_lure: str | None = None
    cache_capacity: int = 5
    purchased_coolers: dict = field(default_factory=dict)

    def __post_init__(self):
        if not self.backpack:
            self.backpack = [
                {"name": "wad", "category": "bait", "quantity": 1, "equipped": self.selected_bait == "wad"},
                {"name": "Old Rod", "category": "rod", "quantity": 1, "equipped": self.selected_rod == "Old Rod"},
            ]
        if self.selected_bait is None:
            self.selected_bait = "wad"
        if not self.selected_rod:
            self.selected_rod = "Old Rod"

    def to_dict(self):
        return {
            "player_name": self.player_name,
            "cache": self.cache,
            "backpack": self.backpack,
            "current_location": self.current_location,
            "unit_system": self.unit_system,
            "money": self.money,
            "favor": self.favor,
            "casts_since_favor_recovery": self.casts_since_favor_recovery,
            "owned_boons": sorted(self.owned_boons),
            "active_boon": self.active_boon,
            "researched_fish": sorted(self.researched_fish),
            "greeting_decks": self.greeting_decks,
            "time_minutes": self.time_minutes,
            "selected_bait": self.selected_bait,
            "selected_rod": self.selected_rod,
            "selected_lure": self.selected_lure,
            "purchased_coolers": self.purchased_coolers,
        }

    @classmethod
    def from_dict(cls, data):
        state = cls()
        for attribute in (
            "player_name",
            "cache",
            "backpack",
            "current_location",
            "unit_system",
            "money",
            "favor",
            "casts_since_favor_recovery",
            "active_boon",
            "greeting_decks",
            "time_minutes",
            "selected_bait",
            "selected_rod",
            "selected_lure",
            "purchased_coolers",
        ):
            if attribute in data:
                setattr(state, attribute, data[attribute])
        state.owned_boons = set(data.get("owned_boons", []))
        state.researched_fish = set(data.get("researched_fish", []))
        state.refresh_cache_capacity()
        return state

    def refresh_cache_capacity(self):
        self.cache_capacity = 5
        for item in self.backpack:
            if item.get("category") != "cooler":
                continue
            name = item.get("name")
            if name == "Small Red Cooler":
                self.cache_capacity = max(self.cache_capacity, 12)
            elif name == "Medium Cooler":
                self.cache_capacity = max(self.cache_capacity, 20)
            elif name == "Name Brand Cooler":
                self.cache_capacity = max(self.cache_capacity, 38)
            elif name == "Industrial Cooler":
                self.cache_capacity = max(self.cache_capacity, 69)

    def formatted_time(self):
        total_minutes = self.time_minutes % (24 * 60)
        hours, minutes = divmod(total_minutes, 60)
        return f"{hours:02d}:{minutes:02d}"

    def advance_time(self, minutes=1):
        self.time_minutes = (self.time_minutes + minutes) % (24 * 60)

    def address_player(self, dialogue):
        if not self.player_name or self.dialogue_random.random() >= 0.15:
            return dialogue
        return f"{self.player_name}! {dialogue}"

    def next_greeting(self, deck_name, greetings):
        remaining = self.greeting_decks.setdefault(deck_name, [])
        previous = self.greeting_decks.get(f"{deck_name}_last")

        if not remaining:
            remaining.extend(greetings)
            if previous in remaining:
                remaining.remove(previous)

        greeting = self.random.choice(remaining)
        remaining.remove(greeting)
        self.greeting_decks[f"{deck_name}_last"] = greeting
        return greeting
