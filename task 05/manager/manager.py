from utils import get_random_users
import json
from models.User import User


class Manager:
    def __init__(self):
        self.users = []


    def get_user(self):
        user_data = get_random_users(10)
        for user in user_data:
            if "full_name" not in user:
                first = user.get("first_name", "")
                last = user.get("last_name", "")
                user["full_name"] = f"{first} {last}".strip()

            if "birth_year" in user and int(user["birth_year"]) < 1990:
                user_obj = User.from_dict(user)
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