from flask import Flask
import os
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Yo'
DB_PATH = os.path.abspath('database.db')


if not os.path.isfile(DB_PATH):
    try:
        sqlite_connection = sqlite3.connect(DB_PATH)
        cur = sqlite_connection.cursor()
        cur.execute('''
            CREATE TABLE users(
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(30),
                email VARCHAR(50),
                password VARCHAR(255)
            );
        ''')
        print("База данных создана и успешно подключена к SQLite")
    except sqlite3.Error as error:
        print(f"Ошибка при подключении к sqlite: {error}")

    finally:
        if sqlite_connection:
            sqlite_connection.close()


import asset.prog.views