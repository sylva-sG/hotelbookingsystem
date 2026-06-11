"""
tests/test_cli.py
Integration tests for CLI command handlers using mock data.
Run with: pytest tests/
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from argparse import Namespace
from models.guest import Guest
from models.room import Room
from models.reservation import Reservation
from main import (
    cmd_add_guest, cmd_add_room, cmd_book_room,
    cmd_checkout, cmd_cancel_booking, find_guest, find_room,
)


@pytest.fixture(autouse=True)
def reset_class_state():
    """Reset all class-level state before each test."""
    Guest.reset()
    Room.reset()
    Reservation.reset()


@pytest.fixture
def sample_data():
    """Provide a fresh guest, room, and reservation for each test."""
    guest = Guest("Zion", "zion@gmail.com", "0712345678")
    room = Room(101, "deluxe", 5000.0)
    reservation = Reservation(guest, room, "2025-07-01", "2025-07-05")
    room.available = False
    return [guest], [room], [reservation]


def test_find_guest(sample_data):
    guests, _, _ = sample_data
    assert find_guest(guests, "Zion") is not None
    assert find_guest(guests, "Nobody") is None

def test_find_room(sample_data):
    _, rooms, _ = sample_data
    assert find_room(rooms, 101) is not None
    assert find_room(rooms, 999) is None

def test_add_guest(tmp_path, monkeypatch):
    import utils.storage as storage
    monkeypatch.setattr(storage, "DATA_FILE", str(tmp_path / "database.json"))
    guests, rooms, reservations = [], [], []
    args = Namespace(name="Alice", email="alice@test.com", phone="0700000000")
    guests, _, _ = cmd_add_guest(args, guests, rooms, reservations)
    assert len(guests) == 1
    assert guests[0].name == "Alice"

def test_add_duplicate_guest(tmp_path, monkeypatch, sample_data):
    import utils.storage as storage
    monkeypatch.setattr(storage, "DATA_FILE", str(tmp_path / "database.json"))
    guests, rooms, reservations = sample_data
    args = Namespace(name="Zion", email="zion2@gmail.com", phone="")
    result, _, _ = cmd_add_guest(args, guests, rooms, reservations)
    assert len(result) == 1

def test_add_room(tmp_path, monkeypatch):
    import utils.storage as storage
    monkeypatch.setattr(storage, "DATA_FILE", str(tmp_path / "database.json"))
    guests, rooms, reservations = [], [], []
    args = Namespace(number=201, type="double", price=4000.0)
    _, rooms, _ = cmd_add_room(args, guests, rooms, reservations)
    assert len(rooms) == 1
    assert rooms[0].number == 201

def test_book_room(tmp_path, monkeypatch):
    import utils.storage as storage
    monkeypatch.setattr(storage, "DATA_FILE", str(tmp_path / "database.json"))
    guest = Guest("Bob", "bob@test.com")
    room = Room(202, "single", 3000.0)
    guests, rooms, reservations = [guest], [room], []
    args = Namespace(guest="Bob", room=202, checkin="2025-08-01", checkout="2025-08-03")
    _, _, reservations = cmd_book_room(args, guests, rooms, reservations)
    assert len(reservations) == 1
    assert room.available is False

def test_checkout_reservation(tmp_path, monkeypatch, sample_data):
    import utils.storage as storage
    monkeypatch.setattr(storage, "DATA_FILE", str(tmp_path / "database.json"))
    guests, rooms, reservations = sample_data
    args = Namespace(id=reservations[0].reservation_id)
    cmd_checkout(args, guests, rooms, reservations)
    assert reservations[0].status == "checked-out"
    assert rooms[0].available is True

def test_cancel_reservation(tmp_path, monkeypatch, sample_data):
    import utils.storage as storage
    monkeypatch.setattr(storage, "DATA_FILE", str(tmp_path / "database.json"))
    guests, rooms, reservations = sample_data
    args = Namespace(id=reservations[0].reservation_id)
    cmd_cancel_booking(args, guests, rooms, reservations)
    assert reservations[0].status == "cancelled"
    assert rooms[0].available is True