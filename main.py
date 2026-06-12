import argparse
from datetime import datetime
from utils.storage import load_data, save_data
from models.guest import Guest
from models.room import Room
from models.reservation import Reservation
from utils.id_generator import get_next_id
from utils.auth import login, logout, register, get_current_user

from utils.decorators import login_required, admin_required



# GUEST

from utils.auth import login, logout, register, get_current_user
# imports
from utils.auth import login, register, logout, get_current_user
...


# HELPERS 

class SimpleArgs:
    def __init__(self, name=None, email=None, number=None, room_type=None):
        self.name = name
        self.email = email
        self.number = number
        self.room_type = room_type


class SimpleRes:
    def __init__(self, email, room_id, check_in, check_out):
        self.email = email
        self.room_id = room_id
        self.check_in = check_in
        self.check_out = check_out



# MENU FUNCTION BELOW

def interactive_menu():
    ...

def interactive_menu():

    while True:

        user = get_current_user()

        print("\n===== HOTEL SYSTEM =====")

        
        # NOT LOGGED IN MENU
       
        if not user:
            print("1. Register")
            print("2. Login")
            print("3. Exit")

            choice = input("Choose: ")

            if choice == "1":
                username = input("Username: ")
                password = input("Password: ")
                register(username, password, "user")

            elif choice == "2":
                username = input("Username: ")
                password = input("Password: ")
                login(username, password)

            elif choice == "3":
                break

            else:
                print("Invalid choice")

       
        # LOGGED IN MENU
        
        else:
            print(f"Logged in as: {user.username} ({user.role})")

           
            # ADMIN MENU
            
            if user.role == "admin":

                print("1. Add Guest")
                print("2. List Guests")
                print("3. Add Room")
                print("4. List Rooms")
                print("5. Add Reservation")
                print("6. List Reservations")
                print("7. Logout")
                print("8. Exit")

                choice = input("Choose: ")

                if choice == "1":
                    name = input("Guest name: ")
                    email = input("Email: ")

                    class Args: pass
                    args = Args()
                    args.name = name
                    args.email = email

                    add_guest(args)

                elif choice == "2":
                    list_guests(None)

                elif choice == "3":
                    number = input("Room number: ")
                    room_type = input("Room type: ")

                    class Args: pass
                    args = Args()
                    args.number = int(number)
                    args.room_type = room_type

                    add_room(args)

                elif choice == "4":
                    list_rooms(None)

                elif choice == "5":
                    email = input("Guest email: ")
                    room_id = input("Room ID: ")
                    check_in = input("Check in (YYYY-MM-DD): ")
                    check_out = input("Check out (YYYY-MM-DD): ")

                    class Args: pass
                    args = Args()
                    args.email = email
                    args.room_id = int(room_id)
                    args.check_in = check_in
                    args.check_out = check_out

                    add_reservation(args)

                elif choice == "6":
                    list_reservations(None)

                elif choice == "7":
                    logout()

                elif choice == "8":
                    break

                else:
                    print("Invalid choice")

            # -------------------------
            # USER MENU (READ ONLY)
            # -------------------------
            else:

                print("1. List Guests")
                print("2. List Rooms")
                print("3. List Reservations")
                print("4. Logout")
                print("5. Exit")

                choice = input("Choose: ")

                if choice == "1":
                    list_guests(None)

                elif choice == "2":
                    list_rooms(None)

                elif choice == "3":
                    list_reservations(None)

                elif choice == "4":
                    logout()

                elif choice == "5":
                    break

                else:
                    print("Invalid choice")
def parse_date(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d")

def is_room_booked(data, room_id, new_check_in, new_check_out):

    new_check_in = parse_date(new_check_in)
    new_check_out = parse_date(new_check_out)

    for r in data["reservations"]:

        if r["room_id"] != room_id:
            continue

        existing_check_in = parse_date(r["check_in"])
        existing_check_out = parse_date(r["check_out"])

        # overlap condition
        if (new_check_in < existing_check_out and new_check_out > existing_check_in):
            return True

    return False
def add_guest(args):
    data = load_data()

    guest = Guest(
        args.name,
        args.email,
        get_next_id(data["guests"])
    )

    data["guests"].append(guest.to_dict())

    save_data(data)

    print(f"Guest {args.name} added successfully")
def list_reservations(args):
    data = load_data()

    if not data["reservations"]:
        print("No reservations found")
        return

    for r in data["reservations"]:

        guest = get_guest_by_id(data, r["guest_id"])
        room = get_room_by_id(data, r["room_id"])

        guest_name = guest["name"] if guest else "Unknown Guest"
        room_number = room["room_number"] if room else "Unknown Room"

        print(
            f"Reservation #{r['id']} | "
            f"Guest: {guest_name} | "
            f"Room: {room_number} | "
            f"{r['status']}"
        )
def get_guest_by_id(data, guest_id):
    return next((g for g in data["guests"] if g["id"] == guest_id), None)


def get_room_by_id(data, room_id):
    return next((r for r in data["rooms"] if r["id"] == room_id), None)


def list_guests(args):
    data = load_data()

    if not data["guests"]:
        print("No guests found")
        return

    for g in data["guests"]:
        print(f"ID: {g['id']} | Name: {g['name']} | Email: {g['email']}")


# =========================
# ROOM
# =========================

def add_room(args):
    data = load_data()

    room = Room(
        args.number,
        args.room_type,
        get_next_id(data["rooms"])
    )

    data["rooms"].append(room.to_dict())

    save_data(data)

    print(f"Room {args.number} added successfully")

def list_rooms(args):
    data = load_data()

    if not data["rooms"]:
        print("No rooms found")
        return

    for r in data["rooms"]:
        print(r)


# =========================
# RESERVATION
# =========================

def add_reservation(args):
    data = load_data()

    guest = next(
        (g for g in data["guests"] if g["email"] == args.email),
        None
    )

    room = next(
        (r for r in data["rooms"] if r["id"] == args.room_id),
        None
    )

    if not guest:
        print("Guest not found")
        return

    if not room:
        print("Room not found")
        return

    if is_room_booked(
        data,
        room["id"],
        args.check_in,
        args.check_out
    ):
        print("Room already booked for these dates")
        return

    reservation = Reservation(
        guest["id"],
        room["id"],
        args.check_in,
        args.check_out,
        get_next_id(data["reservations"])
    )

    data["reservations"].append(reservation.to_dict())

    save_data(data)

    print("Reservation created successfully")

# =========================
# CLI SETUP
# =========================

def main():
    parser = argparse.ArgumentParser(description="Hotel Booking System CLI")
    subparsers = parser.add_subparsers(dest="command")


    # =========================
    # GUEST COMMANDS
    # =========================

    add_guest_parser = subparsers.add_parser("add-guest")
    add_guest_parser.add_argument("--name", required=True)
    add_guest_parser.add_argument("--email", required=True)
    add_guest_parser.set_defaults(
    func=lambda args: admin_required(add_guest)(args)
)

    list_guest_parser = subparsers.add_parser("list-guests")
    list_guest_parser.set_defaults(
    func=lambda args: admin_required(list_guests)(args)
)


    
    # ROOM COMMANDS (ADMIN ONLY)
    

    add_room_parser = subparsers.add_parser("add-room")
    add_room_parser.add_argument("--number", type=int, required=True)
    add_room_parser.add_argument("--room_type", required=True)

    add_room_parser.set_defaults(
        func=lambda args: admin_required(add_room)(args)
    )

    list_room_parser = subparsers.add_parser("list-rooms")
    list_room_parser.set_defaults(func=list_rooms)
    list_res_parser = subparsers.add_parser("list-reservations")
    list_res_parser.set_defaults(
    func=lambda args: admin_required(list_reservations)(args)
)
    # RESERVATION (LOGIN REQUIRED)
  

    add_res_parser = subparsers.add_parser("add-reservation")
    add_res_parser.add_argument("--name", required=True)
    add_res_parser.add_argument("--email", required=True)
    add_res_parser.add_argument("--room_id", type=int, required=True)
    add_res_parser.add_argument("--check_in", required=True)
    add_res_parser.add_argument("--check_out", required=True)
    
    add_res_parser.set_defaults(
        func=lambda args: login_required(add_reservation)(args)
    )


    
    # AUTH COMMANDS
   

    register_parser = subparsers.add_parser("register")
    register_parser.add_argument("--username", required=True)
    register_parser.add_argument("--password", required=True)
    register_parser.add_argument("--role", default="user")
    register_parser.set_defaults(
        func=lambda args: register(args.username, args.password, args.role)
    )

    login_parser = subparsers.add_parser("login")
    login_parser.add_argument("--username", required=True)
    login_parser.add_argument("--password", required=True)
    login_parser.set_defaults(
        func=lambda args: login(args.username, args.password)
    )

    logout_parser = subparsers.add_parser("logout")
    logout_parser.set_defaults(func=lambda args: logout())


    # =========================
    # EXECUTE
    # =========================

    args = parser.parse_args()

    if hasattr(args, "func"):
     args.func(args)
    else:
     interactive_menu()

if __name__ == "__main__":
    main()