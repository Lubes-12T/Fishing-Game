import json
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from pathlib import Path

try:
    from PIL import Image, ImageTk
except ImportError:  # pragma: no cover - Pillow is optional but recommended for JPG art.
    Image = None
    ImageTk = None

import game_rules
from game_state import GameState
from fish_data import (
    BOON_COST,
    BOON_DATA,
    CELIA_GREETINGS,
    FAVOR_CATCH_PENALTY,
    FAVOR_CHANGE_LIMIT,
    FAVOR_POINTS_PER_STEP,
    FAVOR_RECOVERY_CASTS,
    FAVOR_SYMBOL,
    FISH_DATA,
    HARBOR_BUTTON_HEIGHT,
    HARBOR_BUTTON_WIDTH,
    LOCATIONS,
    MIN_CATCH_CHANCE,
    MOLLY_GREETINGS,
    RARITY_COLORS,
    RUPERT_GODFREY_GREETINGS,
    RUPERT_GODFREY_NAME,
    RUPERT_GREETINGS,
    STORE_ITEMS,
)

# Tkinter screens and callbacks for the fishing game.

game_state = GameState()
SAVE_PATH = Path(__file__).resolve().parent / "save_game.json"
active_catch_window = None
active_catch_actions = {}


def save_game(show_confirmation=False):
    try:
        with SAVE_PATH.open("w", encoding="utf-8") as save_file:
            json.dump(game_state.to_dict(), save_file, indent=2)
    except OSError as error:
        messagebox.showerror(
            "Save failed",
            f"The game could not be saved: {error}",
            parent=globals().get("root"),
        )
        return False

    if show_confirmation:
        messagebox.showinfo("Game Saved", "Your progress has been saved.", parent=root)
    return True


def handle_game_key(event):
    key = event.keysym.lower()
    catch_is_open = (
        active_catch_window is not None
        and active_catch_window.winfo_exists()
    )

    if key == "f" and not catch_is_open:
        fish()
        return "break"
    if key in {"r", "k"} and catch_is_open:
        action = active_catch_actions.get(key)
        if action is not None:
            action()
            return "break"

def fish_for_location(location):
    return game_rules.fish_for_location(location)

def catch_random_fish():
    fish_bonuses = {}
    for item_name in (game_state.selected_bait, game_state.selected_lure):
        item = get_store_item(item_name)
        if item is None:
            continue
        for fish_name, bonus in item.get("fish_bonus", {}).items():
            fish_bonuses[fish_name] = fish_bonuses.get(fish_name, 0.0) + bonus
    return game_rules.catch_random_fish(
        game_state.current_location,
        game_state.active_boon,
        game_state.random,
        fish_bonuses
    )

def calculate_fish_points(weight_kg, size_cm):
    return game_rules.calculate_fish_points(weight_kg, size_cm)

def median_fish_points(location):
    return game_rules.median_fish_points(location)

def lower_quartile_fish_points(location):
    return game_rules.lower_quartile_fish_points(location)

def favor_change_for_fish(specimen):
    return game_rules.favor_change_for_fish(specimen)

def favor_loss_for_fish(specimen):
    return game_rules.favor_loss_for_fish(specimen, game_state.active_boon)

def favor_loss_for_dump(specimen):
    return game_rules.favor_loss_for_dump(specimen, game_state.active_boon)

def fish_is_marketable(specimen):
    return game_rules.fish_is_marketable(specimen)

def generate_specimen(fish_name):
    return game_rules.generate_specimen(
        fish_name,
        game_state.current_location,
        game_state.active_boon,
        game_state.random
    )

def calculate_fish_value(fish_name, weight_kg, size_cm):
    return game_rules.calculate_fish_value(fish_name, weight_kg, size_cm)

def sale_payout(specimen):
    return game_rules.sale_payout(specimen, game_state.active_boon)

def format_money(amount):
    return game_rules.format_money(amount)

def format_weight(weight_kg):
    return game_rules.format_weight(weight_kg, game_state.unit_system)

def format_size(size_cm):
    return game_rules.format_size(size_cm, game_state.unit_system)


def normalize_item_name(name):
    if name is None:
        return ""
    return str(name).strip().lower()


def get_store_item(item_name):
    if item_name is None:
        return None
    normalized = normalize_item_name(item_name)
    for name, data in STORE_ITEMS.items():
        if normalize_item_name(name) == normalized:
            return data
    return STORE_ITEMS.get(item_name)


def get_cache_capacity():
    capacity = 5
    for item in game_state.backpack:
        item_data = get_store_item(item.get("name"))
        if item_data and item_data.get("category") == "cooler":
            capacity = max(capacity, int(item_data.get("capacity", 5)))
    return capacity


def get_equipment_bonus(location=None, fish_name=None):
    total = 0.0
    selected_items = [game_state.selected_bait, game_state.selected_rod, game_state.selected_lure]
    for item_name in selected_items:
        if not item_name:
            continue
        item_data = get_store_item(item_name)
        if item_data is None:
            continue
        total += float(item_data.get("bonus", 0.0))
        if location:
            total += float(item_data.get("location_bonus", {}).get(location, 0.0))
        if fish_name:
            total += float(item_data.get("fish_bonus", {}).get(fish_name, 0.0))
    return total


def calculate_cast_success_chance():
    if game_state.current_location == "Harbor":
        return 0.0
    return game_rules.calculate_cast_success_chance(
        0.58,
        get_equipment_bonus(location=game_state.current_location),
    )


def load_character_image(path, target_size=None, master=None):
    """Load a portrait image from disk, including JPGs, while keeping Tk compatibility."""
    resolved_path = Path(path)
    if Image is not None and ImageTk is not None and resolved_path.suffix.lower() in {'.jpg', '.jpeg', '.png', '.bmp', '.gif', '.webp'}:
        image = Image.open(resolved_path)
        if target_size is not None:
            image = image.resize(target_size, Image.LANCZOS)
        photo = ImageTk.PhotoImage(image, master=master)
        return photo
    return tk.PhotoImage(file=str(resolved_path), master=master)


def add_character_portrait(parent, path, master):
    photo = load_character_image(path, target_size=(240, 320), master=master)
    image_label = tk.Label(parent, image=photo, text="")
    image_label.image = photo
    image_label.pack(pady=(0, 8))
    return image_label


def add_character_dialogue(parent, text, wraplength):
    dialogue_label = tk.Label(
        parent,
        text=game_state.address_player(text),
        font=("Arial", 11),
        foreground="#FFFFFF",
        background="#000000",
        wraplength=wraplength,
        justify="center",
        padx=10,
        pady=8,
        relief=tk.SOLID,
        borderwidth=1,
    )
    dialogue_label.pack(fill="x", padx=4)
    return dialogue_label


# ------------------------------------------------------------
# Unit Conversion / Display
# ------------------------------------------------------------

# ------------------------------------------------------------
# UI Actions
# ------------------------------------------------------------

def change_location(location):

    game_state.current_location = location

    location_label.config(text=location)
    description_label.config(text=LOCATIONS[location])
    fishing_title.config(text=location if location == "Harbor" else "Fishing")
    if location == "Harbor":
        fish_button.pack_forget()
        harbor_actions_frame.pack(pady=10)
        last_catch.config(text="Welcome to the harbor.")
    else:
        harbor_actions_frame.pack_forget()
        fish_button.pack(before=last_catch, pady=20)
        last_catch.config(text="Ready to fish.")

    update_cache()

def fish():
    """Catch a fish and display its specimen information."""

    if game_state.current_location == "Harbor":
        return

    catch_chance = calculate_cast_success_chance()
    if game_state.favor < 0:
        catch_chance = max(
            MIN_CATCH_CHANCE,
            min(catch_chance, 1 + game_state.favor * FAVOR_CATCH_PENALTY)
        )
    if game_state.random.random() >= catch_chance:
        last_catch.config(
            text=f"No bite this time. {FAVOR_SYMBOL} Favor: {game_state.favor} | Gear bonus: {get_equipment_bonus(location=game_state.current_location):+.2f}"
        )
        return

    game_state.casts_since_favor_recovery += 1
    if game_state.casts_since_favor_recovery >= FAVOR_RECOVERY_CASTS:
        game_state.favor += 1
        game_state.casts_since_favor_recovery = 0
        update_favor()

    fish_name = catch_random_fish()
    specimen = generate_specimen(fish_name)
    extra_specimen = None
    if game_state.active_boon == "Plenty" and game_state.random.random() < 0.25:
        extra_fish_name = catch_random_fish()
        extra_specimen = generate_specimen(extra_fish_name)

    show_catch_window(specimen, extra_specimen)

def show_catch_window(specimen, next_specimen=None):
    """Display the catch and let the player keep or release it."""
    global active_catch_window, active_catch_actions

    catch_window = tk.Toplevel(root)
    active_catch_window = catch_window
    catch_window.title("You Caught Something!")
    catch_window.geometry("360x330")
    catch_window.resizable(False, False)

    name_label = tk.Label(
        catch_window,
        text=specimen["name"],
        font=("Arial", 20, "bold"),
        fg=RARITY_COLORS.get(specimen["rarity"], "#222222")
    )
    name_label.pack(pady=(25, 5))

    rarity_label = tk.Label(
        catch_window,
        text=f"Rarity: {specimen['rarity']}",
        font=("Arial", 12, "bold")
    )
    rarity_label.pack(pady=5)

    stats = tk.Label(
        catch_window,
        text=(
            f"Weight: {format_weight(specimen['weight_kg'])}\n"
            f"Size: {format_size(specimen['size_cm'])}\n"
            f"Points: {specimen['points']:.1f} "
            f"(location median: {specimen['median_points']:.1f})\n"
            f"Market: {'Accepted' if fish_is_marketable(specimen) else 'Not accepted'}\n"
            f"Market value: {format_money(specimen['value'])}"
        ),
        font=("Arial", 12),
        justify="center"
    )
    stats.pack(pady=15)

    button_frame = tk.Frame(catch_window)
    button_frame.pack(pady=10)

    def keep_fish():
        global active_catch_window, active_catch_actions

        if len(game_state.cache) >= get_cache_capacity():
            messagebox.showwarning(
                "Cache Full",
                f"Your cache is full ({get_cache_capacity()} fish). "
                "Release this catch or visit the Harbor to sell fish."
            )
            return

        favor_loss = favor_loss_for_fish(specimen)
        if favor_loss:
            game_state.favor -= favor_loss
            update_favor()

        game_state.cache.append(specimen)
        last_catch.config(
            text=f"Kept: {specimen['name']} "
                 f"({format_weight(specimen['weight_kg'])}, "
                 f"{format_size(specimen['size_cm'])}) - "
                 f"Market value: {format_money(specimen['value'])}"
                 + (f" | Favor -{favor_loss}" if favor_loss else "")
        )
        update_cache()
        active_catch_window = None
        active_catch_actions = {}
        catch_window.destroy()
        if next_specimen is not None:
            show_catch_window(next_specimen)

    def release_fish():
        global active_catch_window, active_catch_actions

        favor_gain = favor_change_for_fish(specimen)
        game_state.favor += favor_gain
        update_favor()
        last_catch.config(
            text=f"Released: {specimen['name']} | Favor +{favor_gain}"
        )
        active_catch_window = None
        active_catch_actions = {}
        catch_window.destroy()
        if next_specimen is not None:
            show_catch_window(next_specimen)

    keep_button = tk.Button(
        button_frame,
        text="KEEP",
        width=12,
        height=2,
        command=keep_fish,
        state=tk.NORMAL if len(game_state.cache) < get_cache_capacity() else tk.DISABLED
    )
    keep_button.grid(row=0, column=0, padx=8)

    release_button = tk.Button(
        button_frame,
        text="RELEASE",
        width=12,
        height=2,
        command=release_fish
    )
    release_button.grid(row=0, column=1, padx=8)

    active_catch_actions = {"k": keep_fish, "r": release_fish}
    catch_window.protocol("WM_DELETE_WINDOW", release_fish)
    catch_window.transient(root)
    catch_window.grab_set()

def update_cache():
    """Refresh the cache display and capacity summary."""
    cache_list.delete(0, tk.END)
    cache_value = sum(specimen["value"] for specimen in game_state.cache)
    count_label.config(
        text=f"Fish in cache: {len(game_state.cache)} / {get_cache_capacity()} | Value: {format_money(cache_value)}"
    )

    if not game_state.cache:
        cache_list.insert(tk.END, "Cache is empty.")
        return

    for index, specimen in enumerate(game_state.cache, start=1):
        cache_list.insert(
            tk.END,
            f"{index}. {specimen['name']} | "
            f"{format_weight(specimen['weight_kg'])} | "
            f"{format_size(specimen['size_cm'])} | "
            f"{specimen['rarity']}"
        )

def update_balance():
    balance_label.config(text=f"Balance: {format_money(game_state.money)}")


def update_time_label():
    game_state.advance_time(1)
    time_label.config(text=f"Time: {game_state.formatted_time()}")
    root.after(1000, update_time_label)


def update_favor():
    favor_label.config(text=f"{FAVOR_SYMBOL} Favor: {game_state.favor}")

def update_active_boon():
    active_boon_label.config(text=f"Active boon: {game_state.active_boon or 'None'}")

def get_rupert_greeting():
    return game_state.next_greeting("rupert", RUPERT_GREETINGS)

def get_molly_greeting():
    return game_state.next_greeting("molly", MOLLY_GREETINGS)

def get_rupert_godfrey_greeting():
    return game_state.next_greeting("rupert_godfrey", RUPERT_GODFREY_GREETINGS)

def celia_greeting():
    tier = "low" if game_state.favor < 0 else "high" if game_state.favor >= 50 else "normal"
    return game_state.next_greeting(
        f"celia_{tier}",
        CELIA_GREETINGS[tier]
    )

def open_ruins():
    """Open the Ruins boon shop and let the player manage one active boon."""

    ruins_window = tk.Toplevel(root)
    ruins_window.title("The Ruins")
    ruins_window.geometry("850x650")
    ruins_window.minsize(760, 600)

    tk.Label(
        ruins_window,
        text="The Ruins",
        font=("Arial", 20, "bold")
    ).pack(anchor="w", padx=18, pady=(14, 6))

    content_frame = tk.Frame(ruins_window)
    content_frame.pack(fill="both", expand=True, padx=18, pady=(0, 18))

    celia_frame = tk.Frame(content_frame, width=280)
    celia_frame.pack(side=tk.LEFT, fill="y", padx=(0, 18))

    tk.Label(
        celia_frame,
        text="Celia",
        font=("Arial", 16, "bold")
    ).pack(pady=(0, 8))
    tk.Label(
        celia_frame,
        text="Favor Trader",
        font=("Arial", 10, "italic")
    ).pack(pady=(0, 8))

    celia_image_path = Path(__file__).resolve().parent / "Images" / "nymph1.jpg"
    add_character_portrait(celia_frame, celia_image_path, ruins_window)
    add_character_dialogue(celia_frame, celia_greeting(), wraplength=250)

    shop_frame = tk.Frame(content_frame)
    shop_frame.pack(side=tk.LEFT, fill="both", expand=True)

    balance_label = tk.Label(
        shop_frame,
        text=f"{FAVOR_SYMBOL} Favor: {game_state.favor}    Active boon: {game_state.active_boon or 'None'}",
        font=("Arial", 12, "bold")
    )
    balance_label.pack(anchor="w", pady=(0, 10))

    tk.Label(
        shop_frame,
        text=f"Choose a boon. Each new boon costs {BOON_COST} Favor.",
        font=("Arial", 11)
    ).pack(anchor="w", pady=(0, 5))

    boon_list = tk.Listbox(shop_frame, height=8, exportselection=False)
    boon_list.pack(fill="x", pady=(0, 10))
    for boon_name in BOON_DATA:
        boon_list.insert(tk.END, boon_name)

    description_label = tk.Label(
        shop_frame,
        text="Select a boon to read its effect.",
        font=("Arial", 11),
        justify="left",
        anchor="nw",
        wraplength=500,
        height=3
    )
    description_label.pack(fill="x", pady=(0, 10))

    status_label = tk.Label(shop_frame, text="", font=("Arial", 10))
    status_label.pack(anchor="w", pady=(0, 8))

    def refresh_shop():
        balance_label.config(
            text=f"{FAVOR_SYMBOL} Favor: {game_state.favor}    "
                 f"Active boon: {game_state.active_boon or 'None'}"
        )
        selection = boon_list.curselection()
        if selection:
            selected_name = boon_list.get(selection[0])
            description_label.config(
                text=(
                    f"{BOON_DATA[selected_name]['description']}\n"
                    f"Status: {'Owned' if selected_name in game_state.owned_boons else 'Not owned'}"
                )
            )
            if selected_name in game_state.owned_boons:
                action_button.config(
                    text="ACTIVE" if selected_name == game_state.active_boon else "ACTIVATE",
                    state=(
                        tk.DISABLED
                        if selected_name == game_state.active_boon
                        else tk.NORMAL
                    )
                )
            else:
                action_button.config(
                    text=f"BUY FOR {BOON_COST} FAVOR",
                    state=(
                        tk.NORMAL if game_state.favor >= BOON_COST else tk.DISABLED
                    )
                )
        else:
            description_label.config(text="Select a boon to read its effect.")
            action_button.config(state=tk.DISABLED)

    def on_boon_selected(event=None):
        status_label.config(text="")
        refresh_shop()

    def purchase_or_activate():

        selection = boon_list.curselection()
        if not selection:
            return
        boon_name = boon_list.get(selection[0])

        if boon_name in game_state.owned_boons:
            game_state.active_boon = boon_name
            status_label.config(text=f"{boon_name} is now active.")
            refresh_shop()
            update_favor()
            update_active_boon()
            return

        if game_state.favor < BOON_COST:
            status_label.config(text=f"You need {BOON_COST} Favor to buy a boon.")
            return

        game_state.favor -= BOON_COST
        game_state.owned_boons.add(boon_name)
        update_favor()

        if game_state.active_boon is None:
            game_state.active_boon = boon_name
            status_label.config(text=f"Purchased and activated {boon_name}.")
        elif messagebox.askyesno(
            "Boon Purchased",
            f"You bought {boon_name}. Switch from {game_state.active_boon} to {boon_name}?\n\n"
            "Choose No to keep your current boon active."
        ):
            game_state.active_boon = boon_name
            status_label.config(text=f"{boon_name} is now active.")
        else:
            status_label.config(
                text=f"{boon_name} added to your collection. {game_state.active_boon} remains active."
            )

        refresh_shop()
        update_active_boon()

    button_frame = tk.Frame(shop_frame)
    button_frame.pack(anchor="e", pady=(4, 0))
    action_button = tk.Button(
        button_frame,
        text="BUY",
        width=20,
        command=purchase_or_activate,
        state=tk.DISABLED
    )
    action_button.pack(side=tk.LEFT, padx=(0, 8))
    tk.Button(
        button_frame,
        text="CLOSE",
        width=12,
        command=ruins_window.destroy
    ).pack(side=tk.LEFT)

    boon_list.bind("<<ListboxSelect>>", on_boon_selected)
    boon_list.selection_set(0)
    refresh_shop()
    ruins_window.transient(root)
    ruins_window.grab_set()

def dump_cache():
    """Completely reset the cache and game state."""

    if not game_state.cache:
        messagebox.showinfo(
            "Cache Empty",
            "There are no fish to dump."
        )
        return

    answer = messagebox.askyesno(
        "Dump All Fish",
        "This will discard every fish in your cache and cost twice "
        "the Favor releasing them would earn.\n\n"
        "Your cache will be completely emptied.\n\n"
        "Continue?"
    )

    if not answer:
        return

    favor_loss = sum(
        favor_loss_for_dump(specimen)
        for specimen in game_state.cache
    )
    game_state.favor -= favor_loss
    game_state.cache.clear()
    update_favor()
    update_cache()

    last_catch.config(
        text=f"All fish dumped. Cache reset. Favor -{favor_loss}."
    )

def toggle_units():
    """Switch between metric and imperial."""

    if game_state.unit_system == "imperial":
        game_state.unit_system = "metric"
    else:
        game_state.unit_system = "imperial"

    unit_button.config(
        text=f"Units: {'Metric' if game_state.unit_system == 'metric' else 'Imperial'}"
    )

    update_cache()

def open_market():
    """Open the market where selected cached fish can be sold."""
    market_window = tk.Toplevel(root)
    market_window.title("Fish Market")
    market_window.geometry("980x700")
    market_window.minsize(850, 620)

    tk.Label(
        market_window,
        text="Fish Market",
        font=("Arial", 20, "bold")
    ).pack(anchor="w", padx=18, pady=(14, 4))

    market_balance_label = tk.Label(
        market_window,
        text=f"Your balance: {format_money(game_state.money)}",
        font=("Arial", 12, "bold")
    )
    market_balance_label.pack(anchor="w", padx=18, pady=(0, 10))

    content_frame = tk.Frame(market_window)
    content_frame.pack(fill="both", expand=True, padx=18)

    rupert_frame = tk.Frame(content_frame, width=280)
    rupert_frame.pack(side=tk.LEFT, fill="y", padx=(0, 18))

    tk.Label(
        rupert_frame,
        text="Rusty",
        font=("Arial", 16, "bold")
    ).pack(pady=(0, 8))

    rupert_image_path = Path(__file__).resolve().parent / "Images" / "buyer1.jpg"
    add_character_portrait(rupert_frame, rupert_image_path, market_window)
    add_character_dialogue(rupert_frame, get_rupert_greeting(), wraplength=250)

    market_panel = tk.Frame(content_frame)
    market_panel.pack(side=tk.LEFT, fill="both", expand=True)

    tk.Label(
        market_panel,
        text="Select fish to sell or dump. Below-quartile fish are not accepted:",
        font=("Arial", 11)
    ).pack(anchor="w", pady=(0, 5))

    list_frame = tk.Frame(market_panel)
    list_frame.pack(fill="both", expand=True)

    market_list = tk.Listbox(
        list_frame,
        selectmode=tk.EXTENDED,
        exportselection=False,
        font=("Arial", 10),
        height=14
    )
    market_scrollbar = tk.Scrollbar(
        list_frame,
        orient=tk.VERTICAL,
        command=market_list.yview
    )
    market_list.config(yscrollcommand=market_scrollbar.set)
    market_list.pack(side=tk.LEFT, fill="both", expand=True)
    market_scrollbar.pack(side=tk.RIGHT, fill="y")

    selected_total_label = tk.Label(
        market_window,
        text=f"Selected total: {format_money(0)}",
        font=("Arial", 12, "bold")
    )
    selected_total_label.pack(anchor="w", padx=18, pady=(10, 5))

    market_status_label = tk.Label(
        market_window,
        text="",
        font=("Arial", 10)
    )
    market_status_label.pack(anchor="w", padx=18)

    def update_selection(event=None):
        selected_indices = market_list.curselection()
        sellable_indices = [
            index for index in selected_indices
            if fish_is_marketable(game_state.cache[index])
        ]
        selected_value = sum(
            sale_payout(game_state.cache[index])
            for index in sellable_indices
        )
        selected_total_label.config(
            text=f"Selected total: {format_money(selected_value)}"
        )
        sell_button.config(
            state=tk.NORMAL if sellable_indices else tk.DISABLED
        )
        dump_selected_button.config(
            state=tk.NORMAL if selected_indices else tk.DISABLED
        )

    def refresh_market_list():
        market_list.config(state=tk.NORMAL)
        market_list.delete(0, tk.END)

        if game_state.cache:
            for specimen in game_state.cache:
                market_status = (
                    "Accepted"
                    if fish_is_marketable(specimen)
                    else "NOT ACCEPTED - DUMP"
                )
                market_list.insert(
                    tk.END,
                    f"{specimen['name']} | {format_weight(specimen['weight_kg'])} | "
                    f"{format_size(specimen['size_cm'])} | "
                    f"{specimen['points']:.1f} pts | {specimen['rarity']} | "
                    f"{format_money(sale_payout(specimen))} | {market_status}"
                )
        else:
            market_list.insert(tk.END, "Cache is empty.")
            market_list.config(state=tk.DISABLED)

        market_balance_label.config(
            text=f"Your balance: {format_money(game_state.money)}"
        )
        update_selection()

    def sell_selected():

        selected_indices = list(market_list.curselection())
        sellable_indices = [
            index for index in selected_indices
            if fish_is_marketable(game_state.cache[index])
        ]
        if not sellable_indices:
            return

        sold_fish = [game_state.cache[index] for index in sellable_indices]
        sale_total = sum(sale_payout(specimen) for specimen in sold_fish)
        selected_set = set(sellable_indices)
        ineligible_count = len(selected_indices) - len(sellable_indices)

        game_state.cache[:] = [
            specimen
            for index, specimen in enumerate(game_state.cache)
            if index not in selected_set
        ]
        game_state.money = round(game_state.money + sale_total, 2)

        update_balance()
        update_cache()
        refresh_market_list()
        market_status_label.config(
            text=(
                f"Sold {len(sold_fish)} fish for {format_money(sale_total)}."
                + (
                    f" {ineligible_count} below-minimum fish remain in your cache."
                    if ineligible_count else ""
                )
            )
        )

    def dump_selected():

        selected_indices = list(market_list.curselection())
        if not selected_indices:
            return

        dumped_fish = [game_state.cache[index] for index in selected_indices]
        favor_loss = sum(
            favor_loss_for_dump(specimen)
            for specimen in dumped_fish
        )
        selected_set = set(selected_indices)
        game_state.cache[:] = [
            specimen
            for index, specimen in enumerate(game_state.cache)
            if index not in selected_set
        ]
        game_state.favor -= favor_loss

        update_favor()
        update_cache()
        refresh_market_list()
        market_status_label.config(
            text=f"Dumped {len(dumped_fish)} fish. Favor -{favor_loss}."
        )

    button_frame = tk.Frame(market_window)
    button_frame.pack(anchor="e", padx=18, pady=(8, 14))

    dump_selected_button = tk.Button(
        button_frame,
        text="DUMP SELECTED",
        width=18,
        command=dump_selected,
        state=tk.DISABLED
    )
    dump_selected_button.pack(side=tk.LEFT, padx=(0, 8))

    sell_button = tk.Button(
        button_frame,
        text="SELL SELECTED",
        width=18,
        command=sell_selected,
        state=tk.DISABLED
    )
    sell_button.pack(side=tk.LEFT, padx=(0, 8))

    close_button = tk.Button(
        button_frame,
        text="CLOSE",
        width=12,
        command=market_window.destroy
    )
    close_button.pack(side=tk.LEFT)

    market_list.bind("<<ListboxSelect>>", update_selection)
    refresh_market_list()
    market_window.transient(root)
    market_window.grab_set()

def open_general_store():
    """Open Rupert Godfrey's store and let the player buy equipment."""
    store_window = tk.Toplevel(root)
    store_window.title("General Store")
    store_window.geometry("900x760")
    store_window.minsize(700, 640)

    tk.Label(
        store_window,
        text="General Store",
        font=("Arial", 20, "bold")
    ).pack(anchor="w", padx=20, pady=(18, 4))

    body_frame = tk.Frame(store_window)
    body_frame.pack(fill="both", expand=True, padx=18, pady=(0, 12))

    character_frame = tk.Frame(body_frame, width=280)
    character_frame.pack(side=tk.LEFT, fill="both", padx=(0, 18))

    tk.Label(
        character_frame,
        text=RUPERT_GODFREY_NAME,
        font=("Arial", 14, "bold")
    ).pack(pady=(0, 6))
    tk.Label(
        character_frame,
        text="Shopkeeper",
        font=("Arial", 10, "italic")
    ).pack(pady=(0, 6))

    store_image_path = Path(__file__).resolve().parent / "Images" / "shopkeeper1.jpg"
    add_character_portrait(character_frame, store_image_path, store_window)
    add_character_dialogue(
        character_frame,
        get_rupert_godfrey_greeting(),
        wraplength=250,
    )

    store_content = tk.Frame(body_frame)
    store_content.pack(side=tk.LEFT, fill="both", expand=True)

    store_balance_label = tk.Label(
        store_content,
        text=f"Your money: {format_money(game_state.money)}",
        font=("Arial", 12, "bold")
    )
    store_balance_label.pack(anchor="w", pady=(0, 10))

    content_frame = tk.Frame(store_content)
    content_frame.pack(fill="both", expand=True, pady=(0, 10))

    item_list = tk.Listbox(content_frame, height=15, width=62, exportselection=False)
    item_list.pack(side=tk.LEFT, fill="both", expand=True)
    item_scroll = tk.Scrollbar(content_frame, orient=tk.VERTICAL, command=item_list.yview)
    item_scroll.pack(side=tk.RIGHT, fill=tk.Y)
    item_list.config(yscrollcommand=item_scroll.set)

    details_frame = tk.Frame(store_content)
    details_frame.pack(fill="x", pady=(0, 10))
    detail_label = tk.Label(details_frame, text="Select an item to see its effect.", justify="left", wraplength=350, anchor="w")
    detail_label.pack(fill="x")

    def refresh_store_items():
        item_list.delete(0, tk.END)
        for item_name in STORE_ITEMS:
            item_data = STORE_ITEMS[item_name]
            if item_data.get("category") == "cooler":
                item_list.insert(tk.END, f"{item_name} - ${item_data['cost']:.2f} - {item_data['description']}")
            else:
                item_list.insert(tk.END, f"{item_name} - ${item_data['cost']:.2f} - {item_data['category'].title()}")

    def show_selected_item(event=None):
        selection = item_list.curselection()
        if not selection:
            detail_label.config(text="Select an item to see its effect.")
            return
        item_name = list(STORE_ITEMS.keys())[selection[0]]
        item = STORE_ITEMS[item_name]
        bonus = item.get("bonus", 0.0)
        effect = f"Cast bonus: {bonus:+.0%}. " if bonus else ""
        locations = item.get("location_bonus", {})
        if locations:
            effect += "Location bonus: " + ", ".join(
                f"{location} {value:+.0%}" for location, value in locations.items()
            ) + ". "
        fish = item.get("fish_bonus", {})
        if fish:
            effect += "Fish preference: " + ", ".join(
                f"{name} +{value:.0%}" for name, value in fish.items()
            ) + ". "
        detail_label.config(text=f"{item_name}: {item['description']} {effect}")

    def buy_selected_item():
        selection = item_list.curselection()
        if not selection:
            return
        item_name = list(STORE_ITEMS.keys())[selection[0]]
        item = STORE_ITEMS[item_name]
        if game_state.money < item["cost"]:
            messagebox.showwarning("Not enough money", f"You need {format_money(item['cost'])} to buy {item_name}.")
            return
        game_state.money -= item["cost"]
        existing = None
        for entry in game_state.backpack:
            if entry.get("name") == item_name:
                existing = entry
                break
        category = item["category"]
        should_equip = category in {"bait", "rod", "lure"}
        if should_equip:
            for entry in game_state.backpack:
                entry_data = get_store_item(entry.get("name"))
                if entry_data and entry_data.get("category") == category:
                    entry["equipped"] = False
        if existing is None:
            game_state.backpack.append({"name": item_name, "category": category, "quantity": 1, "equipped": should_equip})
        else:
            existing["quantity"] += 1
            existing["equipped"] = should_equip
        if category == "bait":
            game_state.selected_bait = item_name
        elif category == "lure":
            game_state.selected_lure = item_name
        elif category == "rod":
            game_state.selected_rod = item_name
        elif category == "cooler":
            game_state.refresh_cache_capacity()
        messagebox.showinfo("Purchase complete", f"Bought {item_name} for {format_money(item['cost'])}.")
        update_cache()
        update_balance()
        store_window.focus_set()

    buy_button = tk.Button(store_content, text="BUY SELECTED", command=buy_selected_item, width=16)
    buy_button.pack(anchor="e")

    item_list.bind("<<ListboxSelect>>", show_selected_item)
    refresh_store_items()
    store_window.transient(root)
    store_window.grab_set()


def open_backpack():
    """Open the player's backpack and manage equipment and consumable items."""
    backpack_window = tk.Toplevel(root)
    backpack_window.title("Backpack")
    backpack_window.geometry("560x420")
    backpack_window.minsize(480, 320)

    tk.Label(
        backpack_window,
        text="Backpack",
        font=("Arial", 18, "bold")
    ).pack(anchor="w", padx=18, pady=(14, 10))

    item_frame = tk.Frame(backpack_window)
    item_frame.pack(fill="both", expand=True, padx=18, pady=(0, 8))

    backpack_list = tk.Listbox(item_frame, height=12, width=62, exportselection=False)
    backpack_list.pack(side=tk.LEFT, fill="both", expand=True)
    backpack_scroll = tk.Scrollbar(item_frame, orient=tk.VERTICAL, command=backpack_list.yview)
    backpack_scroll.pack(side=tk.RIGHT, fill=tk.Y)
    backpack_list.config(yscrollcommand=backpack_scroll.set)

    detail_label = tk.Label(
        backpack_window,
        text="Select an item to see what it does.",
        justify="left",
        wraplength=500,
        anchor="w"
    )
    detail_label.pack(fill="x", padx=18, pady=(0, 8))

    button_frame = tk.Frame(backpack_window)
    button_frame.pack(anchor="e", padx=18, pady=(0, 16))

    def refresh_backpack_items():
        backpack_list.delete(0, tk.END)
        if not game_state.backpack:
            backpack_list.insert(tk.END, "Backpack is empty.")
            backpack_list.config(state=tk.DISABLED)
            return

        backpack_list.config(state=tk.NORMAL)
        for item in game_state.backpack:
            item_name = item.get("name", "Unknown")
            item_data = get_store_item(item_name)
            description = item_data.get("description", "General gear.") if item_data else "General gear."
            equipped = " [EQUIPPED]" if item.get("equipped") else ""
            backpack_list.insert(tk.END, f"{item_name} x{item.get('quantity', 1)}{equipped} - {description}")

    def show_selected_item(event=None):
        selection = backpack_list.curselection()
        if not selection or not game_state.backpack:
            detail_label.config(text="Select an item to see what it does.")
            return
        index = selection[0]
        item = game_state.backpack[index]
        item_data = get_store_item(item.get("name"))
        if item_data is None:
            detail_label.config(text=f"{item.get('name')} is in your backpack.")
            return

        detail_label.config(text=f"{item['name']}: {item_data.get('description', 'No description available.')}")

    def equip_selected_item():
        selection = backpack_list.curselection()
        if not selection or not game_state.backpack:
            return
        item = game_state.backpack[selection[0]]
        item_name = item.get("name")
        item_data = get_store_item(item_name)
        if item_data is None:
            return

        category = item_data.get("category")
        if category in {"bait", "rod", "lure"}:
            for gear in game_state.backpack:
                gear_name = gear.get("name")
                gear_data = get_store_item(gear_name)
                if gear_data and gear_data.get("category") == category:
                    gear["equipped"] = False
            item["equipped"] = True
            if category == "bait":
                game_state.selected_bait = item_name
            elif category == "rod":
                game_state.selected_rod = item_name
            elif category == "lure":
                game_state.selected_lure = item_name
            refresh_backpack_items()
            detail_label.config(text=f"Equipped {item_name}.")
        elif category == "cooler":
            game_state.refresh_cache_capacity()
            refresh_backpack_items()
            detail_label.config(text=f"{item_name} is active. Cache capacity is now {game_state.cache_capacity}.")
        else:
            detail_label.config(text=f"{item_name} has no equip action.")

    def use_selected_item():
        selection = backpack_list.curselection()
        if not selection or not game_state.backpack:
            return
        item = game_state.backpack[selection[0]]
        item_name = item.get("name")
        item_data = get_store_item(item_name)
        if item_data is None:
            return
        if item_data.get("category") in {"bait", "rod", "lure"}:
            equip_selected_item()
            return
        if item_data.get("category") == "cooler":
            game_state.refresh_cache_capacity()
            refresh_backpack_items()
            detail_label.config(text=f"{item_name} increased your cache capacity to {game_state.cache_capacity}.")
            return
        detail_label.config(text=f"{item_name} is ready to use.")

    equip_button = tk.Button(button_frame, text="EQUIP / APPLY", width=18, command=equip_selected_item)
    equip_button.pack(side=tk.LEFT, padx=(0, 8))
    use_button = tk.Button(button_frame, text="USE", width=12, command=use_selected_item)
    use_button.pack(side=tk.LEFT, padx=(0, 8))
    close_button = tk.Button(button_frame, text="CLOSE", width=12, command=backpack_window.destroy)
    close_button.pack(side=tk.LEFT)

    backpack_list.bind("<<ListboxSelect>>", show_selected_item)
    refresh_backpack_items()
    backpack_window.transient(root)
    backpack_window.grab_set()

def open_aquarium():
    """Open the Fishpedia and Molly's research station."""
    aquarium_window = tk.Toplevel(root)
    aquarium_window.title("Aquarium")
    aquarium_window.geometry("1040x700")
    aquarium_window.minsize(900, 620)

    tk.Label(
        aquarium_window,
        text="Aquarium",
        font=("Arial", 20, "bold")
    ).pack(anchor="w", padx=18, pady=(14, 8))

    content_frame = tk.Frame(aquarium_window)
    content_frame.pack(fill="both", expand=True, padx=18, pady=(0, 18))

    molly_frame = tk.Frame(content_frame, width=280)
    molly_frame.pack(side=tk.LEFT, fill="y", padx=(0, 18))
    molly_frame.pack_propagate(False)

    tk.Label(
        molly_frame,
        text="Molly",
        font=("Arial", 16, "bold")
    ).pack(pady=(4, 2))
    tk.Label(
        molly_frame,
        text="Marine Biologist",
        font=("Arial", 10, "italic")
    ).pack(pady=(0, 8))

    molly_image_path = (
        Path(__file__).resolve().parent
        / "Images"
        / "marine biologist_1.jpg"
    )
    add_character_portrait(molly_frame, molly_image_path, aquarium_window)
    add_character_dialogue(molly_frame, get_molly_greeting(), wraplength=250)

    aquarium_tabs = ttk.Notebook(content_frame)
    aquarium_tabs.pack(side=tk.LEFT, fill="both", expand=True)

    fishpedia_tab = tk.Frame(aquarium_tabs)
    research_tab = tk.Frame(aquarium_tabs)
    aquarium_tabs.add(fishpedia_tab, text="Fishpedia")
    aquarium_tabs.add(research_tab, text="Research")

    fishpedia_content = tk.Frame(fishpedia_tab)
    fishpedia_content.pack(fill="both", expand=True, padx=12, pady=12)

    section_frame = tk.Frame(fishpedia_content)
    section_frame.pack(side=tk.LEFT, fill="y")
    tk.Label(
        section_frame,
        text="Sections",
        font=("Arial", 11, "bold")
    ).pack(anchor="w", pady=(0, 5))
    section_list = tk.Listbox(
        section_frame,
        width=24,
        height=20,
        exportselection=False
    )
    section_list.pack(fill="y")

    fish_list_frame = tk.Frame(fishpedia_content)
    fish_list_frame.pack(side=tk.LEFT, fill="y", padx=(12, 0))
    tk.Label(
        fish_list_frame,
        text="Fish",
        font=("Arial", 11, "bold")
    ).pack(anchor="w", pady=(0, 5))
    fish_list = tk.Listbox(
        fish_list_frame,
        width=23,
        height=20,
        exportselection=False
    )
    fish_list.pack(fill="y")

    detail_frame = tk.Frame(fishpedia_content)
    detail_frame.pack(side=tk.LEFT, fill="both", expand=True, padx=(18, 0))
    fish_name_label = tk.Label(
        detail_frame,
        text="Select an unlocked section",
        font=("Arial", 18, "bold"),
        anchor="w",
        justify="left",
        wraplength=340
    )
    fish_name_label.pack(fill="x", pady=(4, 12))
    fish_description_label = tk.Label(
        detail_frame,
        text="",
        font=("Arial", 11),
        justify="left",
        anchor="nw",
        wraplength=340
    )
    fish_description_label.pack(fill="x", pady=(0, 18))
    fish_details_label = tk.Label(
        detail_frame,
        text="",
        font=("Arial", 11),
        justify="left",
        anchor="nw"
    )
    fish_details_label.pack(fill="x")

    section_locations = []
    section_fish_names = []

    def show_selected_fish(event=None):
        selection = fish_list.curselection()
        if not selection:
            return

        fish_name = section_fish_names[selection[0]]
        if fish_name not in game_state.researched_fish:
            fish_name_label.config(text="Species Locked", fg="#555555")
            fish_description_label.config(
                text="Molly has not researched this species yet."
            )
            fish_details_label.config(text="")
            return

        fish_data = FISH_DATA[fish_name]
        min_weight, max_weight = fish_data["weight_kg"]
        min_size, max_size = fish_data["size_cm"]
        fish_name_label.config(
            text=fish_name,
            fg=RARITY_COLORS.get(fish_data["rarity"], "#222222")
        )
        fish_description_label.config(text=fish_data["description"])
        fish_details_label.config(
            text=(
                f"Location: {', '.join(fish_data['locations'])}\n"
                f"Rarity: {fish_data['rarity']}\n"
                f"Typical weight: {format_weight(min_weight)} - "
                f"{format_weight(max_weight)}\n"
                f"Typical size: {format_size(min_size)} - "
                f"{format_size(max_size)}"
            )
        )

    def show_selected_section(event=None):
        selection = section_list.curselection()
        if not selection:
            return

        location = section_locations[selection[0]]
        fish_list.delete(0, tk.END)
        section_fish_names.clear()

        for fish_name in fish_for_location(location):
            status = "" if fish_name in game_state.researched_fish else " (Locked)"
            fish_list.insert(tk.END, f"{fish_name}{status}")
            section_fish_names.append(fish_name)

        if section_fish_names:
            fish_list.selection_set(0)
            show_selected_fish()

    def refresh_sections(selected_location=None, selected_fish=None):
        section_list.delete(0, tk.END)
        section_locations.clear()
        for location in LOCATIONS:
            if location == "Harbor":
                continue
            section_list.insert(tk.END, location)
            section_locations.append(location)

        if section_locations:
            location_index = (
                section_locations.index(selected_location)
                if selected_location in section_locations else 0
            )
            section_list.selection_set(location_index)
            show_selected_section()

            if selected_fish in section_fish_names:
                fish_index = section_fish_names.index(selected_fish)
                fish_list.selection_clear(0, tk.END)
                fish_list.selection_set(fish_index)
                show_selected_fish()

    research_content = tk.Frame(research_tab)
    research_content.pack(fill="both", expand=True, padx=18, pady=16)
    tk.Label(
        research_content,
        text="Specimens available for research",
        font=("Arial", 12, "bold")
    ).pack(anchor="w", pady=(0, 8))
    research_list = tk.Listbox(
        research_content,
        height=15,
        exportselection=False
    )
    research_list.pack(fill="both", expand=True)
    research_status = tk.Label(
        research_content,
        text="",
        font=("Arial", 10),
        anchor="w",
        justify="left",
        wraplength=650
    )
    research_status.pack(fill="x", pady=(8, 6))
    research_button = tk.Button(
        research_content,
        text="GIVE TO MOLLY",
        width=18,
        state=tk.DISABLED
    )
    research_button.pack(anchor="e")

    research_cache_indices = []

    def refresh_research_list():
        research_list.delete(0, tk.END)
        research_cache_indices.clear()
        for cache_index, specimen in enumerate(game_state.cache):
            if specimen["name"] in game_state.researched_fish:
                continue
            research_list.insert(
                tk.END,
                f"{specimen['name']} | {specimen['location']} | "
                f"{format_weight(specimen['weight_kg'])} | "
                f"{format_size(specimen['size_cm'])}"
            )
            research_cache_indices.append(cache_index)

        if research_cache_indices:
            research_status.config(text="")
            research_button.config(state=tk.NORMAL)
        else:
            research_status.config(
                text="No unresearched fish are available for research."
            )
            research_button.config(state=tk.DISABLED)

    def give_fish_to_molly():
        selection = research_list.curselection()
        if not selection:
            return

        cache_index = research_cache_indices[selection[0]]
        specimen = game_state.cache[cache_index]
        location = specimen["location"]
        fish_name = specimen["name"]
        if fish_name in game_state.researched_fish:
            refresh_research_list()
            return

        game_state.cache.pop(cache_index)
        game_state.researched_fish.add(fish_name)
        update_cache()
        refresh_sections(location, fish_name)
        refresh_research_list()
        research_status.config(
            text=f"Molly researched {fish_name}. Its Fishpedia entry is unlocked."
        )

    def update_research_selection(event=None):
        research_button.config(
            state=(
                tk.NORMAL
                if research_list.curselection()
                else tk.DISABLED
            )
        )

    research_button.config(command=give_fish_to_molly)
    research_list.bind("<<ListboxSelect>>", update_research_selection)
    section_list.bind("<<ListboxSelect>>", show_selected_section)
    fish_list.bind("<<ListboxSelect>>", show_selected_fish)
    refresh_sections()
    refresh_research_list()

    aquarium_window.transient(root)
    aquarium_window.grab_set()

# ------------------------------------------------------------
# Main Window
# ------------------------------------------------------------

def prompt_player_name():
    global game_state

    prompt_root = tk.Tk()
    prompt_root.withdraw()

    if SAVE_PATH.exists() and messagebox.askyesno(
        "Saved Game Found",
        "Continue from your saved game? Choosing No starts a new game.",
        parent=prompt_root,
    ):
        try:
            with SAVE_PATH.open("r", encoding="utf-8") as save_file:
                saved_data = json.load(save_file)
            if not isinstance(saved_data, dict):
                raise ValueError("The save file has an invalid format.")
            saved_state = GameState.from_dict(saved_data)
            if not saved_state.player_name:
                raise ValueError("The save does not contain a player name.")
            game_state = saved_state
            prompt_root.destroy()
            return game_state.player_name
        except (OSError, TypeError, ValueError, KeyError) as error:
            messagebox.showwarning(
                "Save Unavailable",
                f"The saved game could not be loaded: {error}",
                parent=prompt_root,
            )

    while True:
        player_name = simpledialog.askstring(
            "Welcome, Angler",
            "What is your name?",
            parent=prompt_root,
        )
        if player_name is None:
            prompt_root.destroy()
            return None

        player_name = player_name.strip()
        if player_name:
            game_state = GameState(player_name=player_name)
            prompt_root.destroy()
            return player_name

        messagebox.showwarning(
            "Name required",
            "Enter a name to start the game.",
            parent=prompt_root,
        )


def close_game():
    save_game()
    root.destroy()


def adjust_developer_stat(attribute, amount):
    if game_state.player_name.strip().casefold() != "bossman":
        return

    if attribute == "money":
        game_state.money = round(game_state.money + amount, 2)
        update_balance()
    elif attribute == "favor":
        game_state.favor += amount
        update_favor()


def main():
    global root, title, time_label, location_frame, location_label, description_label, main_frame, fishing_frame, fishing_title, fish_button, harbor_actions_frame, aquarium_button, market_button, ruins_button, general_store_button, last_catch, cache_frame, cache_title, count_label, cache_list, controls_frame, unit_button, dump_button, balance_label, favor_label, active_boon_label

    player_name = prompt_player_name()
    if player_name is None:
        return
    game_state.player_name = player_name

    root = tk.Tk()
    root.title(f"Fishing Game Demo - {player_name}")
    root.geometry("900x650")
    root.resizable(True, True)
    root.bind_all("<KeyPress>", handle_game_key)

    root_canvas = tk.Canvas(root)
    root_scrollbar = tk.Scrollbar(root, orient="vertical", command=root_canvas.yview)
    root_canvas.configure(yscrollcommand=root_scrollbar.set)
    root_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    root_canvas.pack(side=tk.LEFT, fill="both", expand=True)

    content_frame = tk.Frame(root_canvas)
    root_canvas.create_window((0, 0), window=content_frame, anchor="nw")
    content_frame.configure(padx=20, pady=10)

    def on_content_configure(event):
        root_canvas.configure(scrollregion=root_canvas.bbox("all"))

    def on_mousewheel(event):
        root_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    content_frame.bind("<Configure>", on_content_configure)
    root_canvas.bind_all("<MouseWheel>", on_mousewheel)

    # Title
    title = tk.Label(
        content_frame,
        text="Fishing Game Demo",
        font=("Arial", 24, "bold")
    )
    title.pack(pady=(15, 5))

    time_label = tk.Label(
        content_frame,
        text=f"Time: {game_state.formatted_time()}",
        font=("Arial", 12, "bold")
    )
    time_label.pack(pady=(0, 10))
    root.after(1000, update_time_label)

    # Location buttons
    location_frame = tk.Frame(content_frame)
    location_frame.pack(pady=10)

    for location in LOCATIONS:
        button = tk.Button(
            location_frame,
            text=location,
            width=20,
            height=2,
            command=lambda loc=location: change_location(loc)
        )
        button.pack(side=tk.LEFT, padx=5)

    location_label = tk.Label(
        content_frame,
        text=game_state.current_location,
        font=("Arial", 18, "bold")
    )
    location_label.pack(pady=(10, 2))

    description_label = tk.Label(
        content_frame,
        text=LOCATIONS[game_state.current_location],
        font=("Arial", 11)
    )
    description_label.pack()

    # Main content area
    main_frame = tk.Frame(content_frame)
    main_frame.pack(fill="both", expand=True, pady=15)
    main_frame.grid_columnconfigure(0, weight=1)
    main_frame.grid_columnconfigure(1, weight=0)

    # Fishing section
    fishing_frame = tk.Frame(main_frame, width=500, height=390)
    fishing_frame.grid(row=0, column=0, padx=(0, 18), pady=10, sticky="n")
    fishing_frame.pack_propagate(False)

    fishing_title = tk.Label(
        fishing_frame,
        text="Fishing",
        font=("Arial", 18, "bold")
    )
    fishing_title.pack(pady=20)

    fish_button = tk.Button(
        fishing_frame,
        text="FISH",
        font=("Arial", 20, "bold"),
        width=16,
        height=5,
        bg="#4A90E2",
        fg="white",
        activebackground="#357ABD",
        activeforeground="white",
        command=fish
    )
    fish_button.pack(pady=20)

    harbor_actions_frame = tk.Frame(
        fishing_frame,
        width=280,
        height=220
    )
    harbor_actions_frame.pack_propagate(False)
    aquarium_button = tk.Button(
        harbor_actions_frame,
        text="AQUARIUM",
        width=HARBOR_BUTTON_WIDTH,
        height=HARBOR_BUTTON_HEIGHT,
        font=("Arial", 10),
        command=open_aquarium
    )
    aquarium_button.pack(fill=tk.X, pady=5)

    market_button = tk.Button(
        harbor_actions_frame,
        text="FISH MARKET",
        width=HARBOR_BUTTON_WIDTH,
        height=HARBOR_BUTTON_HEIGHT,
        font=("Arial", 10),
        command=open_market
    )
    market_button.pack(fill=tk.X, pady=5)

    ruins_button = tk.Button(
        harbor_actions_frame,
        text="THE RUINS",
        width=HARBOR_BUTTON_WIDTH,
        height=HARBOR_BUTTON_HEIGHT,
        font=("Arial", 10),
        command=open_ruins
    )
    ruins_button.pack(fill=tk.X, pady=5)

    general_store_button = tk.Button(
        harbor_actions_frame,
        text="GENERAL STORE",
        width=HARBOR_BUTTON_WIDTH,
        height=HARBOR_BUTTON_HEIGHT,
        font=("Arial", 10),
        command=open_general_store
    )
    general_store_button.pack(fill=tk.X, pady=5)

    last_catch = tk.Label(
        fishing_frame,
        text="Ready to fish.",
        font=("Arial", 12),
        wraplength=400
    )
    last_catch.pack(pady=20)

    # Cache section
    cache_frame = tk.Frame(main_frame)
    cache_frame.grid(row=0, column=1, padx=(0, 10), pady=10, sticky="n")

    cache_title = tk.Label(
        cache_frame,
        text="Cache",
        font=("Arial", 18, "bold")
    )
    cache_title.pack(pady=(20, 5))

    count_label = tk.Label(
        cache_frame,
        text=f"Fish in cache: 0 / {get_cache_capacity()}",
        font=("Arial", 11)
    )
    count_label.pack(pady=(0, 5))

    cache_list = tk.Listbox(
        cache_frame,
        width=60,
        height=15,
        font=("Arial", 10)
    )
    cache_list.pack()

    backpack_button = tk.Button(
        cache_frame,
        text="BACKPACK",
        width=18,
        command=open_backpack
    )
    backpack_button.pack(pady=(10, 0))

    # Bottom controls
    controls_frame = tk.Frame(content_frame)
    controls_frame.pack(pady=(0, 15), anchor="center")

    unit_button = tk.Button(
        controls_frame,
        text="Units: Imperial",
        width=18,
        command=toggle_units
    )
    unit_button.grid(row=0, column=0, padx=8)

    dump_button = tk.Button(
        controls_frame,
        text="DUMP ALL FISH",
        width=22,
        command=dump_cache
    )
    dump_button.grid(row=0, column=1, padx=8)

    if game_state.player_name.strip().casefold() == "bossman":
        balance_frame = tk.Frame(controls_frame)
        balance_frame.grid(row=0, column=2, padx=8)
        tk.Button(
            balance_frame,
            text="▲",
            width=2,
            command=lambda: adjust_developer_stat("money", 100),
        ).pack(side=tk.LEFT)
        balance_label = tk.Label(
            balance_frame,
            text=f"Balance: {format_money(game_state.money)}",
            font=("Arial", 11, "bold"),
        )
        balance_label.pack(side=tk.LEFT)
        tk.Button(
            balance_frame,
            text="▼",
            width=2,
            command=lambda: adjust_developer_stat("money", -100),
        ).pack(side=tk.LEFT)

        favor_frame = tk.Frame(controls_frame)
        favor_frame.grid(row=0, column=3, padx=8)
        tk.Button(
            favor_frame,
            text="▲",
            width=2,
            command=lambda: adjust_developer_stat("favor", 10),
        ).pack(side=tk.LEFT)
        favor_label = tk.Label(
            favor_frame,
            text=f"{FAVOR_SYMBOL} Favor: {game_state.favor}",
            font=("Segoe UI Emoji", 11, "bold"),
        )
        favor_label.pack(side=tk.LEFT)
        tk.Button(
            favor_frame,
            text="▼",
            width=2,
            command=lambda: adjust_developer_stat("favor", -10),
        ).pack(side=tk.LEFT)
    else:
        balance_label = tk.Label(
            controls_frame,
            text=f"Balance: {format_money(game_state.money)}",
            font=("Arial", 11, "bold"),
        )
        balance_label.grid(row=0, column=2, padx=8)

        favor_label = tk.Label(
            controls_frame,
            text=f"{FAVOR_SYMBOL} Favor: {game_state.favor}",
            font=("Segoe UI Emoji", 11, "bold"),
        )
        favor_label.grid(row=0, column=3, padx=8)

    active_boon_label = tk.Label(
        controls_frame,
        text="Active boon: None",
        font=("Arial", 10, "bold")
    )
    active_boon_label.grid(row=0, column=4, padx=8)

    save_button = tk.Button(
        controls_frame,
        text="SAVE",
        width=12,
        command=lambda: save_game(show_confirmation=True),
    )
    save_button.grid(row=1, column=0, columnspan=5, pady=(8, 0))

    update_cache()
    root.update_idletasks()
    root_canvas.configure(scrollregion=root_canvas.bbox("all"))
    root.protocol("WM_DELETE_WINDOW", close_game)

    root.mainloop()
