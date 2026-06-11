from models.person import Person

def test_person_creation():
    person = Person("Sylvans", 18)

    assert person.name == "Sylvans"
    assert person.age == 18