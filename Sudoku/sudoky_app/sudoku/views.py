import copy

from flask import render_template, request

from sudoky_app import app
from sudoky_app.sudoku.models import sudoku, cops


@app.route('/', methods=['GET', 'POST'])
def hello():
    cops = copy.copy(sudoku)
    if request.method == 'POST':

        if request.form.get('clear'):
            print('yu')
            # cops = copy.deepcopy(sudoku)
            for i in range(9):
                for j in range(9):
                    cops[i][j] = copy.deepcopy(sudoku[i][j])
            print(cops)
            print(sudoku)


        for i in range(9):
            for j in range(9):
                if cops[i][j] == 0:
                    el = request.form.get(str(i) + str(j))
                    try:
                        cops[i][j] = int(el)
                    except:
                        cops[i][j] = 0






    return render_template('index.html', sudoku=sudoku)