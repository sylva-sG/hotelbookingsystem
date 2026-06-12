from models.guest import Guest
from models.room import Room
from models.reservation import Reservation

def test_reservation_creation():
    guest = Guest("Zion", "zion@gmail.com")
    room = Room(101, "Deluxe")

    reservation = Reservation(
        guest,
        room,
        "2026-06-15",
        "2026-06-20"
    )

    
def test_checkout():

    guest_id = 1
    room_id = 1

    reservation = Reservation(
        guest_id,
        room_id,
        "2026-06-15",
        "2026-06-20"
    )

    reservation.check_out_guest()

    assert reservation.guest_id == guest_id
    assert reservation.room_id == room_id
    assert reservation.status == "Checked Out"