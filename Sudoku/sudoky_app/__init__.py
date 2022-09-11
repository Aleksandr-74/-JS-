from flask import Flask

app = Flask(__name__)

import sudoky_app.sudoku.views
