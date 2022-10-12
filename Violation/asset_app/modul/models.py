import sqlite3

from wtforms import StringField, SubmitField, DateField, SearchField
from wtforms.validators import DataRequired, Length
from flask_wtf import FlaskForm
from asset_app import DB_PATH


class Intruder:
    def __init__(self, name, number_plate):

        self.name = name
        self.number_plate = number_plate
#         self.identifier = identifier
#         self.violations = violations
# self.sum_fine = sum_fine
# self.date_violation = date_violation

class Fine:
    def __init__(self, violations,  sum_fine, date_violation):
        self.violations = violations
        self.sum_fine = sum_fine
        self.date_violation = date_violation


class Violation(FlaskForm):
    name = StringField("Имя", validators=[DataRequired(), Length(min=1, max=30, message=None)])
    number_plate = SearchField("Гос номер", validators=[DataRequired(), Length(min=1, max=6, message=None)])
    violations = StringField('Нарушение', validators=[DataRequired()])
    sum_fine = StringField("Сумма", validators=[DataRequired()])
    date_violations = DateField("Дата нарушения", format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Отправить')


class searchForm(FlaskForm):
    # number_plate = Se("Гос номер", validators=[DataRequired(), Length(min=1, max=6, message=None)])
    pass
def searchFines():
    pass


def addViolation(intruder, fines):
    print('подключится к базе')
    try:
        connection = sqlite3.connect(DB_PATH)
        cur = connection.cursor()
        cur.execute(f'''
                    INSERT INTO fines(name, number_plate, violation, sum_fine, date_violation, date_payment)
                    VALUES('{intruder.name}','{intruder.number_plate}','{fines.violations}',
                            '{fines.sum_fine}', '{fines.date_violation}', Null);
                    ''')
        connection.commit()
        cur.close()
        print('подключится к базе')

    except sqlite3.Error as error:
        print(f'Не удалось подключится к базе: {error}')

    finally:
        if connection:
            connection.close()


def finesUser():
    try:
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        cursor.execute(
            '''
                SELECT fines_id, name, number_plate, violation, sum_fine, date_violation, date_payment	
                FROM fines
            '''
        )

        current_fine = cursor.fetchall()

    except sqlite3.Error as error:
        print('Не удалось подключиться к бд', error)

    finally:
        if connection:
            connection.close()

    return current_fine
