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
        if "@" not in value or "." not in value:
            raise ValueError("Invalid email address")
        self._email = value

    @classmethod
    def get_all_guests(cls):
        return cls._all_guests

    @classmethod
    def reset(cls):
        cls.guest_count = 0
        cls._all_guests = []

    def to_dict(self):
        return {
            "guest_id": self.guest_id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
        }

    @classmethod
    def from_dict(cls, data):
        guest = cls(data["name"], data["email"], data.get("phone"))
        return guest

    def __str__(self):
        return f"Guest ID: {self.guest_id} | {self.name} | {self.email}"