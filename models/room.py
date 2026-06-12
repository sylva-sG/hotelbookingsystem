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

    def __str__(self):
        return(
            f"Room {self.room_number} | "
            f"{self.room_type} |"
            f"Available: {self.available}"
        )
