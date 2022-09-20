from flask_wtf.file import FileAllowed
from wtforms import StringField, SubmitField, TextAreaField, FileField
from wtforms.validators import DataRequired, Length, Email, InputRequired
from flask_wtf import FlaskForm


class UserForm(FlaskForm):
    name = StringField("name: ", validators=[DataRequired(), Length(min=1, max=30, message=None)])
    email = StringField("email: ", validators=[Email()])
    password = StringField("password: ", validators=[InputRequired(), Length(max=30, message=None)])
    submit = SubmitField('Отправить')


class UserFast(FlaskForm):
    name = StringField(validators=[DataRequired(), Length(min=1, max=30, message=None)],
                       render_kw={"placeholder": "Введите имя"})
    headerLogo = StringField(validators=[DataRequired(), Length(min=1, max=255, message=None)],
                             render_kw={"placeholder": "Заголовок поста"})
    date = StringField()
    message = TextAreaField()
    files = FileField(validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Отправить')



listUser = []
listFast = []


class User():
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def out(self):
        return {'name': {self.name}, 'email': {self.email}, 'password': {self.password}}

    def __str__(self):
        return f"name: {self.name};  email: {self.email}; password: {self.password}"
