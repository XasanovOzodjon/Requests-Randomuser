class User:
    def __init__(self, full_name, email, gender, country):
        self.full_name = full_name
        self.email = email
        self.gender = gender
        self.country = country

    def to_dict(self):
        return {
            "full_name": self.full_name,
            "email": self.email,
            "gender": self.gender,
            "country": self.country
        }

    @classmethod
    def from_dict(cls, data):
        try:
            return cls(
                full_name=data["full_name"],
                email=data["email"],
                gender=data["gender"],
                country=data["country"]
            )
        except KeyError as e:
            print(f"Missing key: {e}")
            return None
