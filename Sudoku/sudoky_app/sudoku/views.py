from flask import render_template, request

from sudoky_app import app
from sudoky_app.sudoku.models import sudoku


@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        for i in range(9):
            for j in range(9):
                el = request.form.get(str(i)+str(j))
                print(el)
                if el == '':
                    sudoku[i][j] = 0
                else:
                    sudoku[i][j] = int(el)




        print(sudoku)


    return render_template('index.html', sudoku=sudoku)