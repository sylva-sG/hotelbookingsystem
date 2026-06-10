class Person:
    def __init__(self, name,  age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"name: {self.name}, age: {self.age}"
    
person1 = Person("sylvans", 18)
print(person1)