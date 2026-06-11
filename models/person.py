class Person:
    def __init__(self, name, age=None):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or not value.strip():
            raise ValueError("Name cannot be empty")
        self._name = value.strip()

    def __str__(self):
        return f"Name: {self.name}"