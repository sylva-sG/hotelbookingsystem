import argparse
from models.guest import Guest
from models.room import Room
from models.reservation import Reservation
from utils.storage import load_data, save_data
from types import SimpleNamespace
from utils.display import display_guests, display_rooms


# ======================
# GUEST
# ======================

def add_guest(args):
    data = load_data()

    try:
        guest = Guest(args.name, args.email)
    except ValueError as e:
        print(f"Error: {e}")
        return

    next_id = len(data.get("guests", [])) + 1

    data['guests'].append({
        "id": next_id,
        "name": guest.name,
        "email": guest.email,
        "phone": guest.phone or "-"
    })

    save_data(data)
    print(f"Guest '{guest.name}' added successfully.")


def list_guests(args):
    data = load_data()

    guests = data.get("guests", [])

    if not guests:
        print("No guests found.")
        return

    wrapped = [
        SimpleNamespace(
            guest_id=g["id"],
            name=g["name"],
            email=g["email"],
            phone=g.get("phone", "-")
        )
        for g in guests
    ]

    display_guests(wrapped)


# ======================
# ROOM
# ======================

def add_room(args):
    data = load_data()

    try:
        room = Room(args.number, args.type, args.price)
    except ValueError as e:
        print(f"Error: {e}")
        return

    data["rooms"].append({
        "room_number": room.number,
        "room_type": room.room_type,
        "price": room.price_per_night,
        "available": room.available
    })

    save_data(data)
    print(f"Room {room.number} added successfully.")


def list_rooms(args):
    data = load_data()

    rooms = data.get("rooms", [])

    if not rooms:
        print("No rooms found.")
        return

    wrapped = [
        SimpleNamespace(
            number=r["room_number"],
            room_type=r["room_type"],
            price_per_night=r["price"],
            available=r["available"]
        )
        for r in rooms
    ]

    display_rooms(wrapped)


# ======================
# BOOKING
# ======================

def book_room(args):
    data = load_data()

    guest = next((g for g in data["guests"] if g["email"] == args.email), None)
    room = next((r for r in data["rooms"] if r["room_number"] == args.room), None)

    if not guest:
        print("Guest not found.")
        return

    if not room:
        print("Room not found.")
        return

    if not room["available"]:
        print("Room already booked.")
        return

    reservation = {
        "guest_email": args.email,
        "room_number": args.room,
        "check_in": args.checkin,
        "check_out": args.checkout
    }

    data.setdefault("reservations", []).append(reservation)
    room["available"] = False

    save_data(data)
    print("Booking successful.")


def checkout(args):
    data = load_data()

    reservations = data.get("reservations", [])

    reservation = next(
        (r for r in reservations if r["room_number"] == args.room),
        None
    )

    if not reservation:
        print("Reservation not found.")
        return

    reservations.remove(reservation)

    for room in data.get("rooms", []):
        if room["room_number"] == args.room:
            room["available"] = True
            break

    save_data(data)
    print("Checkout successful.")


def list_reservations(args):
    data = load_data()

    reservations = data.get("reservations", [])

    if not reservations:
        print("No reservations found.")
        return

    for r in reservations:
        print(
            f"{r['guest_email']} | Room {r['room_number']} | "
            f"{r['check_in']} → {r['check_out']}"
        )


# ======================
# CLI
# ======================

def main():
    parser = argparse.ArgumentParser("Hotel Booking System")
    subparsers = parser.add_subparsers(dest="command")

    # guest
    g = subparsers.add_parser("add-guest")
    g.add_argument("--name", required=True)
    g.add_argument("--email", required=True)
    g.set_defaults(func=add_guest)

    lg = subparsers.add_parser("list-guests")
    lg.set_defaults(func=list_guests)

    # room
    r = subparsers.add_parser("add-room")
    r.add_argument("--number", type=int, required=True)
    r.add_argument("--type", required=True)
    r.add_argument("--price", type=float, required=True)
    r.set_defaults(func=add_room)

    lr = subparsers.add_parser("list-rooms")
    lr.set_defaults(func=list_rooms)

    # booking
    b = subparsers.add_parser("book-room")
    b.add_argument("--email", required=True)
    b.add_argument("--room", type=int, required=True)
    b.add_argument("--checkin", required=True)
    b.add_argument("--checkout", required=True)
    b.set_defaults(func=book_room)

    c = subparsers.add_parser("checkout")
    c.add_argument("--room", type=int, required=True)
    c.set_defaults(func=checkout)

    lrsv = subparsers.add_parser("list-reservations")
    lrsv.set_defaults(func=list_reservations)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()