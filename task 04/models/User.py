class User:
    def __init__(self, full_name, email, image_url):
        self.full_name = full_name
        self.email = email
        self.image_url = image_url

    def to_dict(self):
        return {
            "full_name": self.full_name,
            "email": self.email,
            "image_url": self.image_url
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            full_name=data["full_name"],
            email=data["email"],
            image_url=data["image_url"]
        )
