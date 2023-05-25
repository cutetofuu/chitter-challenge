class Peep:
    def __init__(self, id, message, created_at, user_id, name=None, username=None) -> None:
        self.id = id
        self.message = message
        self.created_at = created_at
        self.user_id = user_id
        self.name = name
        self.username = username

    def __repr__(self) -> str:
        return f"Peep({self.id}, {self.message}, {self.created_at}, {self.user_id})"
    
    def __eq__(self, other) -> bool:
        return self.__dict__ == other.__dict__