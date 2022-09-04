class User():
    def __init__(self, email, password):
        self._email = email
        self._password = password

    def out(self):
        return {"email": self._email, "password": self._password}

    def __str__(self):
        return f"email: {self._email}, password: {self._password}"