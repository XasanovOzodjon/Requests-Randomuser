from manager import Manager
from models.User import User


def main():
    manager = Manager()
    manager.save_users("Data/users.json")


if __name__ == "__main__":
    main()