from models.person import Person

class Guest(Person):

    

    def __init__(self, name, email, guest_id=None):
        super().__init__(name, age=None)
        self.id = guest_id
        self.email = email
        self.reservations = []
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "reservations": [res.to_dict() for res in self.reservations]
        }
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
    
