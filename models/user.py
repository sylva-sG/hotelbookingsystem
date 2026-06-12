import hashlib


class User:
    user_count = 0

    def __init__(self, username, password, role="user"):

        User.user_count += 1

        self.id = User.user_count
        self.username = username
        self.password_hash = self._hash_password(password)
        self.role = role

    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password):
        return self.password_hash == hashlib.sha256(password.encode()).hexdigest()

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "password_hash": self.password_hash,
            "role": self.role
        }

    @classmethod
    def from_dict(cls, data):
        user = cls.__new__(cls)
        user.id = data["id"]
        user.username = data["username"]
        user.password_hash = data["password_hash"]
        user.role = data["role"]
        return user

    def __str__(self):
        return f"{self.id} | {self.username} | {self.role}"