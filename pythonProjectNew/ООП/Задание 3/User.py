class User():
    def __init__(self):
        self.__email, self.__password = input('Введите email и пароль\n').split()
    def out(self):
        return {'email': self.__email, 'password': self.__password}
    def info(self):
        print (f'email:{self.__email}, password:{self.__password}')