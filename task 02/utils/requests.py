import requests


def get_random_users(count=1):
    response = requests.get(f"https://randomuser.me/api/?results={count}")
    if response.status_code == 200:
        return get_user(response.json())
    return -1

def get_user(user):
    result = []
    for user_info in user["results"]:
        result.append({
            "full_name": f"{user_info['name']['first']} {user_info['name']['last']}",
            "gender": user_info["gender"],
            "email": user_info["email"],
            "country": user_info["location"]["country"]
        })
    return result
