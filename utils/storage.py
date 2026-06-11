import json
import os

DATA_FILE = "data/database.json"

DEFAULT_DATA = {
    "guests": [],
    "rooms": [],
    "reservations": []
}

def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        save_data(DEFAULT_DATA)
        return DEFAULT_DATA
    except json.JSONDecodeError:
        print("Warning: database.json is corrupted. Starting fresh.")
        save_data(DEFAULT_DATA)
        return DEFAULT_DATA

def save_data(data):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)