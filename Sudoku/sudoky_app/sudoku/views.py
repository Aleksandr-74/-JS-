from flask import render_template, request

from sudoky_app import app
from sudoky_app.sudoku.models import sudoku, cops, game, chekFilled


@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        if request.form.get('clear'):
           for i in range(9):
               for j in range(9):
                   if cops[i][j] == 0:
                       sudoku[i][j] = 0


        for i in range(9):
            for j in range(9):
                if sudoku[i][j] == 0:
                    try:
                        sudoku[i][j] = int(request.form.get(str(i) + str(j)))
                    except:
                        sudoku[i][j] = 0

        if chekFilled(sudoku):
            res = game(sudoku)
        else:
            res ='Игра не закончена!'
    return render_template('index.html', sudoku=sudoku, res=res)