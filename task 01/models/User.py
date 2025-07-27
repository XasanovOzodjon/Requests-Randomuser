class User:
    def __init__(self, first_name, last_name, age, email, gender, phone, street, city, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.gender = gender
        self.phone = phone
        self.address = {
            "street": street,
            "city": city,
            "country": country
        }
        
        
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    
    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "gender": self.gender,
            "email": self.email,
            "phone": self.phone,
            "address": {
                "street": self.address["street"],
                "city": self.address["city"],
                "country": self.address["country"]
            }
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            first_name=data["first_name"],
            last_name=data["last_name"],
            age=data.get("age", 0),  # Default age to 0 if not provided
            email=data["email"],
            gender=data["gender"],
            phone=data["phone"],
            street=data["address"]["street"],
            city=data["address"]["city"],
            country=data["address"]["country"]
        )
