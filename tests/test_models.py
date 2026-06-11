from models.guest import Guest


def test_guest_creation():

    guest = Guest(
        "Zion",
        "zion@gmail.com"
    )

    assert guest.name == "Zion"
    assert guest.email == "zion@gmail.com"