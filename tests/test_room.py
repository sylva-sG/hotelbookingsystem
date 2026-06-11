from models.room import Room

def test_room_creation():
    room = Room(101, "Deluxe")

    assert room.room_number == 101
    assert room.room_type == "Deluxe"

def test_room_availability():
    room = Room(101, "Deluxe")

    room.available = False

    assert room.available is False