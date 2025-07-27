from utils import get_random_users
import json
from models.User import User


class Manager:
    def __init__(self):
        self.users = []

    # manager.py ichida
    def get_user(self):
        user_data = get_random_users(10)
        for user in user_data:
            # Formatni moslashtirish
            if "full_name" not in user:
                first = user.get("first_name", "")
                last = user.get("last_name", "")
                user["full_name"] = f"{first} {last}".strip()
            # country ni location dan olish
            if "country" not in user and "location" in user and "country" in user["location"]:
                user["country"] = user["location"]["country"]
            # Faqat kerakli kalitlar bo'lsa, User obyektini yaratamiz
            if all(k in user for k in ("full_name", "email", "gender", "country")):
                user_obj = User.from_dict(user)
                if user_obj is not None:
                    self.users.append(user_obj)
    
    def save_users(self, filename):
        with open(filename, 'w') as file:
            result = []
            for user in self.users:
                user_dict = user.to_dict()
                result.append(user_dict)
            json.dump(result, file, indent=4)
            

    def get_users(self):
        return self.users