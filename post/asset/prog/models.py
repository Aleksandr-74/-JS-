import sqlite3

from flask_wtf.file import FileAllowed

from wtforms import StringField, SubmitField, TextAreaField, FileField
from wtforms.validators import DataRequired, Length, Email, InputRequired
from flask_wtf import FlaskForm

from asset import DB_PATH


class UserForm(FlaskForm):
    name = StringField("Имя: ", validators=[DataRequired(), Length(min=1, max=30, message=None)])
    email = StringField("email: ", validators=[Email()])
    password = StringField("Пароль: ", validators=[InputRequired(), Length(max=30, message=None)])
    submit = SubmitField('Отправить')


class UserFast(FlaskForm):
    name = StringField(validators=[DataRequired(), Length(min=1, max=30, message=None)],
                       render_kw={"placeholder": "Введите имя"})
    headerLogo = StringField(validators=[DataRequired(), Length(min=1, max=255, message=None)],
                             render_kw={"placeholder": "Заголовок поста"})
    message = TextAreaField()
    files = FileField(validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Отправить')

def addUser(user):
    try:
        connection = sqlite3.connect(DB_PATH)
        cur = connection.cursor()
        cur.execute(f'''
            INSERT INTO users(name, email, password)
            VALUES('{user.name}','{user.email}','{user.password}')
            ''')
        connection.commit()
        cur.close()

    except sqlite3.Error as error:
        print(f'Не удалось подключится к базе: {error}')

    finally:
        if connection:
            connection.close()




listUser = []
listFast = []


class Fast():
    def __init__(self, name, headerLogo, message,  files, now):
        self.name = name
        self.headerLogo = headerLogo
        self.message = message
        self.files = files
        self.now = now


class User():
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def out(self):
        return {'name': {self.name}, 'email': {self.email}, 'password': {self.password}}

    def __str__(self):
        return f"name: {self.name};  email: {self.email}; password: {self.password}"
