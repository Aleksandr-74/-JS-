n = 9

sudoku = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]

cops =  [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]

copy = {1, 2, 3, 4, 5, 6, 7, 8, 9}



# проверка на заполненость поля
def chekFilled(a):
    for row in a:
        for el in row:
            if el == 0:
                return False
    return True

# Проверка по горизонтали и вертикали
def chek(a):
    for i in range(n):
        row = set(a[i])
        colum = set()
        for j in range(n):
            colum.add(a[j][i])
        if row != copy or colum != copy:
            return False
    return True


# Проверго по квадратам
def chekColum(a):
    colum = set()
    colum2 = set()
    colum3 = set()
    for i in range(n):
        if (len(colum3)) <= n:
            for j in range(3):
                 colum.add(a[i][j])
                 colum2.add(a[i][j + 3])
                 colum3.add(a[i][j + 6])
        else:
            if colum != copy or colum2 != copy or colum3 != copy:
                return False
            else:
                colum = set()
                colum2 = set()
                colum3 = set()
    return True


def game(a):
    if not chek(a):
        return 'Ошибка по горизонтали или вертикали!'
    elif not chekColum(sudoku):
        return 'Ошибка в квадрате'
    else:
        return 'Верно!'
#





if __name__ == '__main__':
    chek(sudoku)






