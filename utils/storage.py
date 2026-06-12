import json

def save_data(data, filename="data/hotel_data.json"):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def load_data(filename="data/hotel_data.json"):

    try:
        with open(filename, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return {
            "guests": [],
            "rooms": [],
            "reservations": []
        }
