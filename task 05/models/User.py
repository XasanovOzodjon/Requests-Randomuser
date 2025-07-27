class User:
    def __init__(self, full_name, email, birth_year):
        self.full_name = full_name
        self.birth_year = birth_year
        self.email = email

    def to_dict(self):
        return {
            "full_name": self.full_name,
            "birth_year": self.birth_year,
            "email": self.email
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            full_name=data["full_name"],
            birth_year=data["birth_year"],
            email=data["email"],
        )
