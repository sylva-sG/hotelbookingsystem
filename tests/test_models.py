"""
tests/test_models.py
Unit tests for Guest, Room, and Reservation models.
Run with: pytest tests/
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from models.guest import Guest
from models.room import Room
from models.reservation import Reservation


@pytest.fixture(autouse=True)
def reset_class_state():
    """Reset all class-level state before each test."""
    Guest.reset()
    Room.reset()
    Reservation.reset()


def test_guest_creation():
    guest = Guest("Zion", "zion@gmail.com", "0712345678")
    assert guest.name == "Zion"
    assert guest.email == "zion@gmail.com"
    assert guest.phone == "0712345678"
    assert guest.guest_id == 1

def test_guest_count():
    Guest("Alice", "alice@test.com")
    Guest("Bob", "bob@test.com")
    assert Guest.guest_count == 2

def test_guest_invalid_email():
    with pytest.raises(ValueError):
        Guest("Bad", "not-an-email")

def test_guest_empty_name():
    with pytest.raises(ValueError):
        g = Guest("Valid", "v@v.com")
        g.name = "  "

def test_guest_serialization():
    guest = Guest("Zion", "zion@gmail.com", "0700000000")
    data = guest.to_dict()
    restored = Guest.from_dict(data)
    assert restored.name == "Zion"
    assert restored.email == "zion@gmail.com"

def test_get_all_guests():
    Guest("A", "a@a.com")
    Guest("B", "b@b.com")
    assert len(Guest.get_all_guests()) == 2

def test_room_creation():
    room = Room(101, "Deluxe", 5000.0)
    assert room.number == 101
    assert room.room_type == "deluxe"
    assert room.price_per_night == 5000.0
    assert room.available is True

def test_room_invalid_type():
    with pytest.raises(ValueError):
        r = Room(102, "single")
        r.room_type = "penthouse"

def test_room_negative_price():
    with pytest.raises(ValueError):
        r = Room(103, "double", 3000)
        r.price_per_night = -100

def test_get_available_rooms():
    Room(101, "single", 3000)
    r2 = Room(102, "double", 4000)
    r2.available = False
    available = Room.get_available_rooms()
    assert len(available) == 1
    assert available[0].number == 101

def test_find_by_number():
    Room(201, "suite", 10000)
    found = Room.find_by_number(201)
    assert found is not None
    assert found.room_type == "suite"

def test_room_serialization():
    room = Room(301, "double", 4500)
    data = room.to_dict()
    restored = Room.from_dict(data)
    assert restored.number == 301
    assert restored.price_per_night == 4500

def test_booking():
    guest = Guest("Zion", "zion@gmail.com")
    room = Room(101, "deluxe", 5000)
    res = Reservation(guest, room, "2025-07-01", "2025-07-05")
    assert res.guest.name == "Zion"
    assert res.room.number == 101
    assert res.nights() == 4
    assert res.total_cost() == 20000.0
    assert res.status == "confirmed"

def test_checkout():
    guest = Guest("Zion", "zion@gmail.com")
    room = Room(101, "single", 3000)
    res = Reservation(guest, room, "2025-07-01", "2025-07-03")
    room.available = False
    res.checkout()
    assert res.status == "checked-out"
    assert room.available is True

def test_cancel_reservation():
    guest = Guest("Alice", "alice@test.com")
    room = Room(202, "double", 4000)
    res = Reservation(guest, room, "2025-08-01", "2025-08-03")
    room.available = False
    res.cancel()
    assert res.status == "cancelled"
    assert room.available is True

def test_invalid_status():
    guest = Guest("Bob", "bob@test.com")
    room = Room(303, "suite", 8000)
    res = Reservation(guest, room, "2025-09-01", "2025-09-05")
    with pytest.raises(ValueError):
        res.status = "pending"

def test_reservation_serialization():
    guest = Guest("Zion", "zion@gmail.com")
    room = Room(101, "deluxe", 5000)
    res = Reservation(guest, room, "2025-07-01", "2025-07-05")
    data = res.to_dict()
    restored = Reservation.from_dict(data, [guest], [room])
    assert restored.guest.name == "Zion"
    assert restored.room.number == 101
    assert restored.nights() == 4