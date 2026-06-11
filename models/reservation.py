from datetime import datetime, date


class Reservation:
    reservation_count = 0
    _all_reservations = []
    VALID_STATUSES = ["confirmed", "cancelled", "checked-out"]

    def __init__(self, guest, room, check_in, check_out):
        self.guest = guest
        self.room = room
        self.check_in = check_in
        self.check_out = check_out
        self._status = "confirmed"
        Reservation.reservation_count += 1
        self.reservation_id = Reservation.reservation_count
        Reservation._all_reservations.append(self)

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if value not in self.VALID_STATUSES:
            raise ValueError(f"Status must be one of {self.VALID_STATUSES}")
        self._status = value

    def nights(self):
        checkin = datetime.strptime(self.check_in, "%Y-%m-%d").date()
        checkout = datetime.strptime(self.check_out, "%Y-%m-%d").date()
        return (checkout - checkin).days

    def total_cost(self):
        return self.nights() * self.room.price_per_night

    def checkout(self):
        self.status = "checked-out"
        self.room.available = True

    def cancel(self):
        self.status = "cancelled"
        self.room.available = True

    def is_overdue(self):
        checkout = datetime.strptime(self.check_out, "%Y-%m-%d").date()
        return date.today() > checkout and self.status == "confirmed"

    @classmethod
    def reset(cls):
        cls.reservation_count = 0
        cls._all_reservations = []

    def to_dict(self):
        return {
            "reservation_id": self.reservation_id,
            "guest_id": self.guest.guest_id,
            "room_number": self.room.number,
            "check_in": self.check_in,
            "check_out": self.check_out,
            "status": self.status,
        }

    @classmethod
    def from_dict(cls, data, guests, rooms):
        guest = next(g for g in guests if g.guest_id == data["guest_id"])
        room = next(r for r in rooms if r.number == data["room_number"])
        res = cls(guest, room, data["check_in"], data["check_out"])
        res.status = data["status"]
        return res

    def __str__(self):
        return (
            f"Reservation #{self.reservation_id} | "
            f"{self.guest.name} | "
            f"Room {self.room.number} | "
            f"{self.status}"
        )