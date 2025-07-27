from manager import Manager
from models.User import User


def main():
    manager = Manager()
    manager.get_user()  # Userlarni olish
    manager.save_users("users.json")


if __name__ == "__main__":
    main()