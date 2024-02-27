import numpy as np

# Создание матрицы через нумпи.
matrix = np.full((3,3), ' ', dtype=object)
move = 0
x_o = ['X', 'O']

def draw():
    print("---------------")
    print("* | 1 | 2 | 3 |")
    print("---------------")
    for i, row in enumerate(matrix):
        print(f'{i + 1} | {" | ".join(str(v) for v in row)} |')
        print("---------------")

def check_diagonals(matrix):
    # проверка позиций матрицы
    diagonal = np.diagonal(matrix)
    reversed_diagonal = np.diagonal(np.fliplr(matrix))
    return diagonal, reversed_diagonal

def make_move():
    global move
    if move % 2 == 0:
        print ('Ход КРЕСТИКОВ')
        move_symbol = 'X'
    else:
        print('Ход НОЛИКОВ')
        move_symbol = 'O'

    while True:
        print('Сделайте ход. Введите через пробел номер строки и номер столбца')
        m = input('---> ')
        x_y = m.split(' ')
                
        if len(x_y) != 2:
            print('Неверные данные. Пожалуйста введите два числа от одного до трёх')
            print(x_y)
            continue
        
        for xy in x_y:
            if not(xy.isdigit()):
                print("Введи пожалуйста числа.")

        x, y = list(map(lambda t: int(t) - 1, x_y))

        if 2 < int(x) or int(x) < 0:
            print("Номер строки введён не верно")
            continue

        if 2 < y and y < 0:
            print("Номер строки введён не верно")
            continue
        
        if matrix[x, y] != " ":
            print('Эта клетка уже занята. Сюда ходить нельзя.')

        else:
            matrix[x, y] = move_symbol
            break
        # move += 1
        print("ЧЁТО НЕ-ТО")

def check_lines():
    global x_o
    for symbol in x_o:
        matches_row_and_collumns = matrix == symbol
        rows_with_symbol = matches_row_and_collumns.all(axis=0)
        column_with_symbol = matches_row_and_collumns.all(axis=1)

        diagonal = np.diagonal(matrix)
        reversed_diagonal = np.diagonal(np.fliplr(matrix))
        all_in_diagonal = np.all(diagonal == symbol)
        all_in_reversed_diagonal = np.all(reversed_diagonal == symbol)

        if True in rows_with_symbol \
            or True in column_with_symbol \
            or all_in_diagonal == True \
            or all_in_reversed_diagonal == True:

            if symbol == 'X': wins = 'КРЕСТИКИ'
            else: wins = 'НОЛИКИ'
            return f"{wins} ПОБЕДИЛИ!!!"
        
        return False

draw()
while  move < 10:
    make_move()
    response = check_lines()
    if response:
        draw()
        print(response)
        exit()
    draw()
    move += 1

print("Ну всё! Ничья...")
