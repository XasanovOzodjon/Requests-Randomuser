
from manager import Manager

def main():
    manager = Manager()
    manager.get_user()  # Userlarni olish
    manager.save_users("Data/young_users.json")  # Faylga yozish

if __name__ == "__main__":
    main()