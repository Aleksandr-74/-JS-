import copy

from click import clear
from flask import render_template, request

from sudoky_app import app
from sudoky_app.sudoku.models import sudoku

@app.route('/', methods=['GET', 'POST'])
def hello():

    copys = copy.deepcopy(sudoku)

    if request.method == 'POST':


        if request.form.get('clear'):
            copys.clear()
            copys = copy.deepcopy(sudoku)
            print(copys)
            print('yu')



        for i in range(9):
            for j in range(9):
                if copys[i][j] == 0:
                    try:
                        copys[i][j] = int(request.form.get(str(i) + str(j)))
                    except:
                        copys[i][j] = 0






    return render_template('index.html', sudoku=copys)