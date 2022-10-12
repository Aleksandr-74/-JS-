import sqlite3

from wtforms import StringField, SubmitField, DateField, SearchField
from wtforms.validators import DataRequired, Length
from flask_wtf import FlaskForm
from asset_app import DB_PATH


class Intruder:
    def __init__(self, name, number_plate):
        self.name = name
        self.number_plate = number_plate
        # self.violation = violation
        # self.date_violation = date_violation

class Fine:
    def __init__(self, violations, sum_fine):
        self.violations = violations
        self.sum_fine = sum_fine



class Violation(FlaskForm):
    name = StringField("Имя", validators=[DataRequired(), Length(min=1, max=30, message=None)])
    number_plate = StringField("Гос номер", validators=[DataRequired(), Length(min=1, max=6, message=None)])
    violations = StringField('Нарушение', validators=[DataRequired()])
    date_violations = DateField("Дата нарушения", format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Отправить')


class SearchForm(FlaskForm):
    number_plate = SearchField("Гос номер", validators=[DataRequired(), Length(min=1, max=6, message=None)])
    submit = SubmitField('Отправить')


def searchFines(number):
    try:
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        cursor.execute(f'''
                SELECT name, number_plate, violation, sum_fine, date_violation, date_payment	
                FROM offense
                WHERE number_plate = '{number}';
            ''')
        current_fine = cursor.fetchall()
    except sqlite3.Error as error:
        print(f'Не удалось подключиться searchFines к бд : {error}')

    finally:
        if connection:
            connection.close()

    return current_fine


def summ():
    try:
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        cursor.execute(
                '''
                 UPDATE offense, violation
                    SET offense.sum_fine = violation.sum_fine
                    WHERE offense.violation = violation.violation;
                
                '''


                )

        connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print(f'Не удалось подключиться summ к бд: {error}')

    finally:
        if connection:
            connection.close()


def addViolation(driver, violation, date_violation):
    print('подключится к базе')
    try:
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        cursor.execute(f'''
            INSERT INTO offense(name, number_plate, violation, sum_fine, date_violation, date_payment)
            VALUES('{driver.name}', '{driver.number_plate}', '{violation}', 
            Null, '{date_violation}', Null);                   
         ''')
        connection.commit()
        cursor.close()
        print('подключится к базе')



    except sqlite3.Error as error:
        print(f'Не удалось подключится addViolation к базе: {error}')

    finally:
        if connection:
            connection.close()


def finesUser():
    try:
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        cursor.execute(
            '''               
                SELECT offense_id, name, number_plate, violation, sum_fine, date_violation, date_payment	
                FROM offense;
                       
            ''')
        current_fine = cursor.fetchall()
        cursor.close()

    except sqlite3.Error as error:
        print(f'Не удалось подключиться finesUser к бд: {error}')

    finally:
        if connection:
            connection.close()

    return current_fine
