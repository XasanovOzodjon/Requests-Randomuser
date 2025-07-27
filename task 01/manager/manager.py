from utils import get_random_user
import json
from models.User import User


class Manager:
    def __init__(self):
        self.users = [self.get_user()]

    def get_user(self):
        user_data = get_random_user()
        if user_data != -1:
            user = User.from_dict(user_data)
            return user

    def load_users(self):
        user_data = get_random_user()
        if user_data != -1:
            user = User.from_dict(user_data)
            self.users.append(user)
    
    def save_users(self, filename):
        with open(f"Data/{filename}", 'w') as file:
            json.dump([user.to_dict() for user in self.users], file, indent=4)

    def get_users(self):
        return self.users