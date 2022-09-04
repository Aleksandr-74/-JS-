import csv


class DataBase:
    def __init__(self, csv, User):
        self.__csv = csv
        self.__user = User


    def authentication(self):
        fieldnames = ['email', 'password']
        reader = csv.DictReader(self.__csv, fieldnames=fieldnames)
        for row in reader:
            if row == self.__user.out():
                return True
            else:
                return False


    # добавления users
    def newUser(self):
        fieldnames = ['email', 'password']
        writer = csv.DictWriter(self.__csv, fieldnames=fieldnames)
        writer.writerow(self.__user.out())
        print('Пользователь добавлен')


    # def passwordChanges(self):
    #     if self.__user != None:
    #         fieldnames = ['email', 'password']
    #         reader = csv.DictReader(self.__csv, fieldnames=fieldnames)
    #         for row in reader:
    #             if row == self.__user:
    #                 row['password'] = 'newPassword'
    #                 writer = csv.DictWriter(self.__csv, fieldnames=fieldnames)
    #                 writer.writerow(row)
    #                 return print('Пароль изменен!')
    #             continue
    #     else:
    #         self.authentication()
    #         self.passwordChanges()


