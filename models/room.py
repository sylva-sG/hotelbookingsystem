class Room:
    room_count = 0
    _all_rooms = []
    VALID_TYPES = ["single", "double", "deluxe", "suite"]

    def __init__(self, number, room_type, price_per_night=0.0):
        self.number = number
        self.room_type = room_type.lower()
        self.price_per_night = price_per_night
        self.available = True
        Room.room_count += 1
        Room._all_rooms.append(self)

    @property
    def room_type(self):
        return self._room_type

    @room_type.setter
    def room_type(self, value):
        if value.lower() not in self.VALID_TYPES:
            raise ValueError(f"Room type must be one of {self.VALID_TYPES}")
        self._room_type = value.lower()

    @property
    def price_per_night(self):
        return self._price_per_night

    @price_per_night.setter
    def price_per_night(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price_per_night = value

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
        return f"Room {self.number} | {self.room_type} | Available: {self.available}"