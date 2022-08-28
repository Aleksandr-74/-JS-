from DataBase import DataBase

out = input('Введит число\n 1 - Добавить пользователя\n 2 - авторизироватся\n 3 - Изменить пароль\n')
if out == '1':
    with open('B:\git\pythonProjectNew\ФАЙЛ\Base.csv', mode='a', newline='') as csvFile:
        dataUser = DataBase(csvFile)
        dataUser.newUser()
elif out == '2':
    with open('B:\git\pythonProjectNew\ФАЙЛ\Base.csv', mode='r', newline='') as csvFile:
        dataUser = DataBase(csvFile)
        dataUser.authentication()
# Изменить пароль
elif out == '3':
    with open('B:\git\pythonProjectNew\ФАЙЛ\Base.csv', mode='+r', encoding='utf-8', newline='') as csvFile:
        dataUser = DataBase(csvFile)
        dataUser.passwordChanges()
