import csv
from User import User

class DataBase:
    def __init__(self, csv):
        self.__csv = csv
        self.__user = {'email': 'ivanov46@gmail.com', 'password': 'qwerty123'}


    def authentication(self):
        self.__user = User()
        fieldnames = ['email', 'password']
        reader = csv.DictReader(self.__csv, fieldnames=fieldnames)
        for row in reader:
            if row == self.__user.out():
                print('Вы авторизовались')
                self.__user.info()
                self.__user = row
                return self.__user
            else:
                continue
        print('Неверный логин или пароль')


    def newUser(self):
        fieldnames = ['email', 'password']
        writer = csv.DictWriter(self.__csv, fieldnames = fieldnames)
        self.__user = User()
        writer.writerow(self.__user.out())
        print('Пользователь добавлен')


    def passwordChanges(self):
        if self.__user != None:
            fieldnames = ['email', 'password']
            reader = csv.DictReader(self.__csv, fieldnames=fieldnames)
            for row in reader:
                if row == self.__user:
                    row['password'] = 'newPassword'
                    writer = csv.DictWriter(self.__csv, fieldnames=fieldnames)
                    writer.writerow(row)
                    return print('Пароль изменен!')
                continue
        else:
            self.authentication()
            self.passwordChanges()





















