from utils.auth import get_current_user

def login_required(func):

    def wrapper(*args, **kwargs):
        user = get_current_user()

        if not user:
            print("You must be logged in to perform this action")
            return

        return func(*args, **kwargs)

    return wrapper
def admin_required(func):

    def wrapper(*args, **kwargs):
        user = get_current_user()

        if not user:
            print("You must be logged in")
            return

        if user.role != "admin":
            print("Admin access required")
            return

        return func(*args, **kwargs)

    return wrapper