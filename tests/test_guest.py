from models.guest import Guest
from models.person import Person
from models.room import Room
from models.reservation import Reservation
import pytest

def test_guest_creation():
    guest = Guest("Zion", "zion@gmail.com")

    assert guest.name == "Zion"
    assert guest.email == "zion@gmail.com"

def test_guest_is_person():
    guest = Guest("Zion", "zion@gmail.com")

    assert isinstance(guest, Person)

def test_invalid_email():
    with pytest.raises(ValueError):
        Guest("Zion", "invalid-email")

def test_add_reservation():
    guest = Guest("Zion", "zion@gmail.com")
    room = Room(101, "Deluxe")

    reservation = Reservation(
        guest,
        room,
        "2026-06-15",
        "2026-06-20"
    )

    guest.add_reservation(reservation)

    assert len(guest.reservations) == 1