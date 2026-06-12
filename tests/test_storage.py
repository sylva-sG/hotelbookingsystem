from utils.storage import load_data

def test_load_data():
    data = load_data()

    assert "guests" in data
    assert "rooms" in data
    assert "reservations" in data

from utils.storage import save_data, load_data

def test_save_data():

    test_data = {
        "guests": [],
        "rooms": [],
        "reservations": []
    }

    save_data(test_data)

    loaded_data = load_data()

    assert loaded_data == test_data