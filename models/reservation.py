from datetime import datetime, date


class Reservation:
    

    def __init__(
        self,
        guest_id,
        room_id,
        check_in,
        check_out,
        reservation_id=None
    ):
        self.id = reservation_id
        self.guest_id = guest_id
        self.room_id = room_id
        self.check_in = check_in
        self.check_out = check_out
        self.status = "Active"
    def to_dict(self):
        return {
            "id": self.id,
            "guest_id": self.guest_id,
            "room_id": self.room_id,
            "check_in": self.check_in,
            "check_out": self.check_out,
            "status": self.status
        }

    def check_out_guest(self):
        self.status = "Checked Out"
    def __str__(self):
     return (
        f"Reservation #{self.id} | "
        f"Guest ID: {self.guest_id} | "
        f"Room ID: {self.room_id} | "
        f"{self.status}"
    )
