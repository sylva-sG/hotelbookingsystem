class Reservation:
     reservation_count = 0

     def __init__(self, guest, room, check_in, check_out):
          Reservation.reservation_count += 1

          self.id = Reservation.reservation_count
          self.guest = guest
          self.room = room

          self.check_in = check_in
          self.check_out = check_out

          self.status = "Booked"

     def check_out_guest(self):
        self.status = "Checked Out"
        self.room.available = True
     def __str__(self):
          return (
            f"Reservation #{self.id} | "
            f"{self.guest.name} | "
            f"Room {self.room.number} | "
            f"{self.status}"
        )