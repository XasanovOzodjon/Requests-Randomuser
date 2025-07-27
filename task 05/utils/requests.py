import requests


def get_random_users(count=1):
    response = requests.get(f"https://randomuser.me/api/?results={count}")
    if response.status_code == 200:
        return get_user(response.json())
    return -1

def get_user(user):
    result = []
    for user_info in user["results"]:
        birth_year = int(user_info["dob"]["date"][:4])  # "1985-03-12T..." => 1985
        result.append({
            "full_name": f"{user_info['name']['first']} {user_info['name']['last']}",
            "email": user_info["email"],
            "birth_year": birth_year,
        })
    return result
