class User:
    def __init__(self, full_name, email, phone, country):
        self.full_name = full_name
        self.email = email
        self.phone = phone
        self.country = country

    def to_dict(self):
        return {
            "full_name": self.full_name,
            "email": self.email,
            "phone": self.phone,
            "country": self.country
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            full_name=data["full_name"],
            email=data["email"],
            phone=data["phone"],
            country=data["country"]
        )
