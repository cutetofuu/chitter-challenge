import re

class User:
    def __init__(self, id, email, password, name, username) -> None:
        self.id = id
        self._email = email
        self._password = password
        self.name = name
        self.username = username

    def __repr__(self) -> str:
        return f"User({self.id}, {self.name}, {self.username})"
    
    def __eq__(self, other) -> bool:
        return self.__dict__ == other.__dict__
    
    def is_valid(self):
        if re.search(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b", self._email) == None:
            return False
        
        if len(self._password) < 8 or re.search("\\W+", self._password) == None:
            return False
        
        if self.name == None or self.name == "":
            return False
        
        if self.username == None or self.username == "":
            return False
        
        return True
    
    def generate_errors(self):
        errors = []
        if self._email == None or self._email == "":
            errors.append("Email can't be blank")
        elif re.search(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b", self._email) == None:
            errors.append("Invalid email")
        
        if self._password == None or self._password == "":
            errors.append("Password can't be blank")
        elif len(self._password) < 8:
            errors.append("Password must be at least 8 characters long")

        if len(self._password) > 0 and re.search("\\W+", self._password) == None:
                errors.append("Password must have at least 1 special character")

        if self.name == None or self.name == "":
            errors.append("Name can't be blank")

        if self.username == None or self.username == "":
            errors.append("Username can't be blank")

        if len(errors) > 0:
            return ", ".join(errors)
        else:
            return None