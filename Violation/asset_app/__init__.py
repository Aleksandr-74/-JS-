from flask import Flask
import os
import sqlite3



DB_PATH = os.path.abspath('dataBase.db')
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Sany'

if not os.path.isfile(DB_PATH):
    try:
        sqlite_connection = sqlite3.connect(DB_PATH)
        cur = sqlite_connection.cursor()
        cur.execute('''
            CREATE TABLE fines(
                fines_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(30),
                number_plate VARCHAR(6),
                violation VARCHAR(255),
                sum_fine DECIMAL(8,2),
                date_violation DATE,
                date_payment DATE	                
            ); 
        ''')
        print("База данных создана и успешно подключена к SQLite")
    except sqlite3.Error as error:
        print(f"Ошибка при подключении к sqlite: {error}")

    finally:
        if sqlite_connection:
            sqlite_connection.close()


import asset_app.modul.views




