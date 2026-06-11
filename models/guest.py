from models.person import Person
print("Import works")
class Guest(Person):

    guest_count = 0

    def __init__(self, name, email):
        super().__init__(name, age=None)
        self.email = email
        Guest.guest_count += 1
        self.id = Guest.guest_count
        self.email = email
        self.reservations = []

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("Invalid email address")
        self._email = value

    def add_reservation(self, reservation):
        self.reservations.append(reservation)
        
    def __str__(self):
        return f"Guest ID: {self.id} | {self.name} | {self.email}"
    
