import argparse
from models.guest import Guest
from models.room import Room
from models.reservation import Reservation
from utils.storage import load_data, save_data

# GUEST
def add_guest(args):
    data = load_data()

    try:
        guest = Guest(args.name, args.email, args.age)
    except ValueError as e:
        print(f"Error: {e}")
        return

    data['guests'].append({
        "id": guest.id,
        "name": guest.name,
        "email": guest.email,
        "age": guest.age
    })    

    save_data(data)
    print(f"Guest '{guest.name}' added successfully with ID {guest.id}.")


def list_guests(args):
    data = load_data()

    if not data['guests']:
        print("No guests found.")
        return

    for g in data['guests']:
        print(f"ID: {g['id']}, Name: {g['name']}, Email: {g['email']}, Age: {g['age']}")       