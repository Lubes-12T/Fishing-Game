# Fishing Game

A Tkinter fishing game organized into data, rules, state, and UI modules.

## Requirements

- Python 3
- Visual Studio Code
- No external Python packages are required.

The game uses Python's built-in `tkinter` GUI library. No external runtime packages are required.

## Run in Visual Studio Code

1. Open this folder in Visual Studio Code.
2. Run `fishing_game.py` using the Python Run button, or open a terminal in this folder and run:

```bash
python fishing_game.py
```

On some systems the command is:

```bash
python3 fishing_game.py
```

## Project Layout

- `fishing_game.py` — application launcher.
- `game_ui.py` — Tkinter screens and UI callbacks.
- `game_state.py` — mutable state for one game session.
- `game_rules.py` — fish generation, scoring, Favor, and market calculations.
- `fish_data.py` — fish, location, boon, and dialogue data.
- `tests/test_game_rules.py` — automated tests for the rule system and state.

## Tests

Run the rule and state tests from this folder:

```bash
python -m unittest discover -s tests -v
```

The game includes Freshwater Lake, Coastal Reef, Open Ocean, and Harbor. Harbor provides the Aquarium, Fish Market, Ruins, and General Store. Aquarium research unlocks individual Fishpedia entries; the Ruins offer Favor boons; and the market accepts eligible fish for money.
