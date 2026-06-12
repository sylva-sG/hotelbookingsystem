class Room:


    def __init__(
    self,
    room_number,
    room_type,
    room_id=None
):
     self.id = room_id
     self.room_number = room_number
     self.room_type = room_type
     self.available = True
    def to_dict(self):
        return {
            "id": self.id,
            "room_number": self.room_number,
            "room_type": self.room_type,
            "available": self.available
        }  
    @property
    def available(self):
        return self._available

    @available.setter
    def available(self, value):
        if not isinstance(value, bool):
            raise ValueError("Available must be True or False")
        self._available = value

    @classmethod
    def get_available_rooms(cls):
        return [r for r in cls._all_rooms if r.available]

    @classmethod
    def get_all_rooms(cls):
        return cls._all_rooms

    @classmethod
    def find_by_number(cls, number):
        for room in cls._all_rooms:
            if room.number == number:
                return room
        return None

    @classmethod
    def reset(cls):
        cls.room_count = 0
        cls._all_rooms = []

    def to_dict(self):
        return {
            "number": self.number,
            "room_type": self.room_type,
            "price_per_night": self.price_per_night,
            "available": self.available,
        }

    @classmethod
    def from_dict(cls, data):
        room = cls(data["number"], data["room_type"], data["price_per_night"])
        room.available = data.get("available", True)
        return room

    def __str__(self):
        return(
            f"Room {self.room_number} | "
            f"{self.room_type} |"
            f"Available: {self.available}"
        )
