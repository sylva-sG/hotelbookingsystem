# 🏨 Hotel Booking System CLI

This is a command-line app that lets you manage hotel guests, rooms, and reservations straight from your terminal. No fancy UI — just type a command and it works.

We built it using Python, and it uses `argparse` for commands and `rich` to make the output look nice in the terminal.

---

## 📁 Project Structure

```
hotelbookingsystem/
├── models/
│   ├── person.py
│   ├── guest.py
│   ├── room.py
│   └── reservation.py
├── utils/
│   ├── storage.py
│   └── display.py
├── tests/
│   ├── test_models.py
│   └── test_cli.py
├── data/
│   └── database.json
├── main.py
├── requirements.txt
└── README.md
```

---

## 🛠 How to Set It Up

First, clone the project and go into the folder:

```bash
git clone <repo-url>
cd hotelbookingsystem
```

Then create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate
```

Then install the dependencies:

```bash
pip install -r requirements.txt
```

That's it — you're ready to go.

---

## 💻 How to Use It

All commands start with `python main.py` followed by what you want to do.

**Add a guest**
```bash
python main.py add-guest --name "Zion" --email "zion@gmail.com" --phone "0712345678"
```

**See all guests**
```bash
python main.py list-guests
```

**Add a room**
```bash
python main.py add-room --number 101 --type deluxe --price 5000
```

**See all rooms**
```bash
python main.py list-rooms
```

**Book a room**
```bash
python main.py book-room --guest "Zion" --room 101 --checkin 2025-07-01 --checkout 2025-07-05
```

**See all reservations**
```bash
python main.py list-reservations
```

**Checkout a guest**
```bash
python main.py checkout --id 1
```

**Cancel a booking**
```bash
python main.py cancel --id 1
```

---

## 🧪 Running the Tests

To check that everything is working:

```bash
pytest tests/
```

---

## 👥 The Team

| Member | What They Did |
|--------|--------------|
| Member 1 | Built the data models (Guest, Room, Reservation) |
| Member 2 | Handled saving and loading data using JSON |
| Member 3 | Built all the CLI commands |
| Member 4 | Wrote the tests, display tables, and this README |

---

## 📦 What You Need

- Python 3.8 or higher
- rich >= 13.0.0
- pytest >= 7.0.0