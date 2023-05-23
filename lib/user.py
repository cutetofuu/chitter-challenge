class User:
    def __init__(self, id, email, password, name, username) -> None:
        self.id = id
        self.email = email
        self.password = password
        self.name = name
        self.username = username

    def __repr__(self) -> str:
        return f"User({self.id}, {self.email}, {self.password}, {self.name}, {self.username})"
    
    def __eq__(self, other) -> bool:
        return self.__dict__ == other.__dict__