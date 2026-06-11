from models.person import Person


class Guest(Person):
    guest_count = 0
    _all_guests = []

    def __init__(self, name, email, phone=None):
        super().__init__(name)
        self.email = email
        self.phone = phone
        Guest.guest_count += 1
        self.guest_id = Guest.guest_count
        self.reservations = []
        Guest._all_guests.append(self)

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