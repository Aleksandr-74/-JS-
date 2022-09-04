from flask import Flask, render_template, request
import csv
from DataBase import DataBase
from User import User


app = Flask(__name__)

app.route("/")


@app.route("/")
@app.route("/citi", methods=['GET', 'POST'])
def citis():
    if request.method == 'POST':
         with open('B:\git\Test\\flask\static\Base.csv', mode='r+', encoding='UTF-8', newline='') as csv:
            email = request.form.get('email')
            password = request.form.get('password')
            if email != "" in password != "":
                user = User(email, password)
                print(user)
                uz = DataBase(csv, user)
                if uz.authentication():
                    outs = f'user:  {email} авторизировался'
                    return render_template('index.html', outs=outs,  user=user, email=email)
                outs = f"user: {email} добавден!"
                uz.newUser()
                return render_template('index.html', outs=outs)
            outs = "Введите данные!"
            return render_template('index.html', outs=outs)
    return render_template('index.html')


@app.route('/citi/small')
def parserSmall():
    with open('B:\git\Test\\flask\static\small towns.csv', mode='r', encoding='utf-8', newline='') as f:
        reader = csv.reader(f)
        return render_template("small towns.html", reader=reader)


@app.route('/citi/medium')
def parserMedium():
    with open('B:\git\Test\\flask\static\medium cities.csv', mode='r', encoding='utf-8', newline='') as f:
        reader = csv.reader(f)
        return render_template("medium cities.html", reader=reader)


@app.route('/citi/largest')
def parserLargest():
    with open('B:\git\Test\\flask\static\largest cities.csv', mode='r', encoding='utf-8', newline='') as f:
        reader = csv.reader(f)
        return render_template("largest cities.html", reader=reader)


@app.route('/citi/millionaires')
def parserMillionaires():
    with open('B:\git\Test\\flask\static\cities millionaires.csv', mode='r', encoding='utf-8', newline='') as f:
        reader = csv.reader(f)
        return render_template("cities millionaires.html", reader=reader)


@app.route('/citi/bigСities')
def parserBigСcities():
    with open('B:\git\Test\\flask\static\\bigСcities.csv', mode='r', encoding='utf-8', newline='') as f:
        reader = csv.reader(f)
        return render_template("bigСcities.html", reader=reader)


@app.route('/citi/big_cities')
def parserBig_cities():
    with open('B:\git\Test\\flask\static\\big_cities.csv', mode='r', encoding='utf-8', newline='') as f:
        reader = csv.reader(f)
        return render_template('big_cities.html', reader=reader)


# @app.route('/', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         with open('B:\git\Test\\flask\static\Base.csv', mode='r+', encoding='UTF-8', newline='') as csv:
#             email = request.form.get('email')
#             password = request.form.get('password')
#             user = User(email, password)
#             print(user)
#             uz = DataBase(csv, user)
#             if uz.authentication():
#                 return render_template('forms.html', user=user, email=email)
#
#             uz.newUser()
#             print(f"{user} добавден!")
#
#     return render_template('forms.html')

if __name__ == '__main__':
    app.run()
