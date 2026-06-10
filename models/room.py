class Room:

    room_count = 0

    def __init__(self, room_number, room_type,):
        Room.room_count += 1

        self.id = Room.room_count
        self.room_number = room_number
        self.room_type = room_type
        self.available = True
        
    @property
    def available(self):
        return self._available
    
    @available.setter
    def available(self, value):
        if not isinstance(value, bool):
            raise ValueError("Available must be True or False")
        self._available = value

    def __str__(self):
        return(
            f"Room {self.room_number} | "
            f"{self.room_type} |"
            f"Available: {self.available}"
        )
room1 = Room(101, "Deluxe")
print(room1)