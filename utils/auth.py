import json
from models.user import User
from utils.storage import load_data, save_data

SESSION_FILE = "data/session.json"

current_user = None


def save_session(user):

    with open(SESSION_FILE, "w") as file:
        json.dump(
            {
                "username": user.username,
                "role": user.role
            },
            file,
            indent=4
        )


def load_session():

    try:
        with open(SESSION_FILE, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return {}


def register(username, password, role="user"):

    data = load_data()

    data.setdefault("users", [])

    for u in data["users"]:
        if u["username"] == username:
            print("Username already exists")
            return

    user = User(username, password, role)

    data["users"].append(user.to_dict())

    save_data(data)

    print("User registered successfully")


def login(username, password):

    global current_user

    data = load_data()

    data.setdefault("users", [])

    for u in data["users"]:

        user = User.from_dict(u)

        if user.username == username and user.check_password(password):

            current_user = user
            save_session(user)

            print(f"Logged in as {user.username}")
            return True

    print("Invalid credentials")
    return False


def logout():

    global current_user

    current_user = None

    with open(SESSION_FILE, "w") as file:
        json.dump({}, file)

    print("Logged out successfully")


def get_current_user():

    session = load_session()

    if not session:
        return None

    return User(
        session["username"],
        "",
        session["role"]
    )