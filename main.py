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


# ROOM

def add_room(args):
    data = load_data()

    try:
        room = Room(args.number, args.type)
    except ValueError as e:
        print(f"Error: {e}")
        return

    data["rooms"].append({
        "id": room.id,
        "room_number": room.room_number,
        "room_type": room.room_type,
        "price": room.price
    })

    save_data(data)
    print(f"Room added successfully")

def list_rooms(args):    
    data = load_data()

    rooms = data.get("rooms", [])

    if not rooms:
        print("No rooms found.")
        return

    for room in rooms:
        status = "Available" if room["available"] else "Booked"
        print(f"Room {room['room_number']} | "
              f"Type: {room['room_type']} | "
              f"Status: {status}"
  )
        
def book_room(args):
    data = load_data()

    guest_email = args.email
    room_number = args.room

    guest = next((g for g in data['guests'] if g['email'] == guest_email), None)

    if not guest:
        print(f"No guest found.")
        return
    
    room = next((r for r in data['rooms'] if r['room_number'] == room_number), None)

    if not room:
        print(f"No room found.")
        return
    
    if not room['available']:
        print(f"Room {room_number} is already booked.")
        return
    
    reservation = {
        "guest_email": guest_email,
        "room_number": room_number,
        "check_in": args.check_in,
        "check_out": args.check_out
    }

    data.setdefault("reservations", []).append(reservation)
    room['available'] = False

    save_data(data)
    print(f"Room booked successfully.")

def checkout(args):
    data = load_data()

    room_number = args.room

    reservations = data.get("reservations", [])

    reservation = next(
        (r for r in reservations if r['room_number'] == room_number), None
    )

    if not reservation:
        print(f"No reservation found.")
        return
    
    reservations.remove(reservation)

    for room in data.get("rooms", []):
        if room['room_number'] == room_number:
            room['available'] = True
            break

    save_data(data)
    print(f"Checked out successfully.")


def list_reservations(args):
    data = load_data()

    reservations = data.get("reservations", [])

    if not reservations:
        print("No reservations found.")
        return

    for reservation in reservations:
        print(f"Guest Email: {reservation['guest_email']} | "
              f"Room Number: {reservation['room_number']} | "
              f"Check-in: {reservation['check_in']} | "
              f"Check-out: {reservation['check_out']}"
        )    

        
    