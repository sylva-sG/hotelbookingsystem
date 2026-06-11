"""
tests/test_cli.py
Integration tests for CLI command handlers.
Run with: pytest tests/
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from main import add_guest, add_room, book_room, checkout, list_guests, list_rooms, list_reservations
from argparse import Namespace


@pytest.fixture
def tmp_data(tmp_path, monkeypatch):
    import utils.storage as storage
    db = tmp_path / "database.json"
    monkeypatch.setattr(storage, "DATA_FILE", str(db))
    return str(db)


def test_add_guest(tmp_data):
    args = Namespace(name="Alice", email="alice@test.com")
    add_guest(args)
    from utils.storage import load_data
    data = load_data()
    assert len(data["guests"]) == 1
    assert data["guests"][0]["name"] == "Alice"


def test_add_room(tmp_data):
    args = Namespace(number=101, type="deluxe", price=5000.0)
    add_room(args)
    from utils.storage import load_data
    data = load_data()
    assert len(data["rooms"]) == 1
    assert data["rooms"][0]["room_number"] == 101


def test_book_room(tmp_data):
    add_guest(Namespace(name="Bob", email="bob@test.com"))
    add_room(Namespace(number=202, type="single", price=3000.0))
    args = Namespace(email="bob@test.com", room=202, checkin="2025-08-01", checkout="2025-08-03")
    book_room(args)
    from utils.storage import load_data
    data = load_data()
    assert len(data["reservations"]) == 1


def test_checkout_room(tmp_data):
    add_guest(Namespace(name="Bob", email="bob@test.com"))
    add_room(Namespace(number=202, type="single", price=3000.0))
    book_room(Namespace(email="bob@test.com", room=202, checkin="2025-08-01", checkout="2025-08-03"))
    checkout(Namespace(room=202))
    from utils.storage import load_data
    data = load_data()
    assert data["rooms"][0]["available"] is True


def test_book_unavailable_room(tmp_data):
    add_guest(Namespace(name="Bob", email="bob@test.com"))
    add_room(Namespace(number=202, type="single", price=3000.0))
    book_room(Namespace(email="bob@test.com", room=202, checkin="2025-08-01", checkout="2025-08-03"))
    book_room(Namespace(email="bob@test.com", room=202, checkin="2025-08-01", checkout="2025-08-03"))
    from utils.storage import load_data
    data = load_data()
    assert len(data["reservations"]) == 1


def test_book_nonexistent_guest(tmp_data):
    add_room(Namespace(number=202, type="single", price=3000.0))
    book_room(Namespace(email="nobody@test.com", room=202, checkin="2025-08-01", checkout="2025-08-03"))
    from utils.storage import load_data
    data = load_data()
    assert len(data.get("reservations", [])) == 0