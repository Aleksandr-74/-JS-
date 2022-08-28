class User():
    def __init__(self):
        self._email, self._password = input('Введите email и пароль\n').split()

    def out(self):
        return {"email": self._email, "password": self._password}

    def info(self):
        print(f"email: {self._email}, password: {self._password}")