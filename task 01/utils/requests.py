
import requests

def get_random_user():
    response = requests.get("https://randomuser.me/api/")
    if response.status_code == 200:
        return get_user(response.json())
    return -1

def get_user(user):
    if "results" in user and len(user["results"]) > 0:
        user_info = user["results"][0]

        return {
            "first_name": user_info["name"]["first"],
            "last_name": user_info["name"]["last"],
            "gender": user_info["gender"],
            "email": user_info["email"],
            "phone": user_info["phone"],
            "address": {
                "street": user_info["location"]["street"]["number"],
                "city": user_info["location"]["city"],
                "country": user_info["location"]["country"]
  }
}
    return -1
