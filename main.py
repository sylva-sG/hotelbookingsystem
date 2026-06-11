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