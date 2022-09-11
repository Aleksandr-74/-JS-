from flask import render_template, request

from sudoky_app import app
from sudoky_app.sudoku.models import sudoku


@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        liste = request.form.get('test')
        print(*liste)
    return render_template('index.html', sudoku=sudoku)