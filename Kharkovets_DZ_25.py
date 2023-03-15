# ДЗ 25. Транспонировать матрицу
#
# s1 = Транспортировка матрицы
# s2 = С помощью функции случайных чисел будет создана и
#      транспортирована матрица методом поворота на 90 градусов по
#      часовой стрелке.
# s3 = Введите параметры матрицы (числа от 2 до 20):
# s4 = количество строк:
# s5 = количество столбцов:
# s6 = Исходный вариант матрицы:
# s7 = Матрица, повернутая на 90 градусов по часовой стрелке:
# s8 = Недопустимые параметры. Перезапустите программу!

import random

s1 = "\n\t\tMatrix transportation\n"
s2 = """
    Using the random number function, a matrix will be created and 
    transported by rotating 90 degrees clockwise.\n"""
s3 = "\tEnter the matrix parameters (numbers from 2 to 20):"
s4 = "number of rows = "
s5 = "number of columns = "
s6 = "The original version of the matrix:\n"
s7 = "\nMatrix rotated 90 degrees clockwise:\n"
s8 = "Invalid parameters. RESTART THE PROGRAM!"

print(s1.upper(), s2, s3)
rows = input(s4)
columns = input(s5)

try:
    if rows.isdigit() and columns.isdigit():

        r1 = int(rows)
        c1 = int(columns)
        if 1 < r1 < 21 and 1 < c1 < 21:
            matrix = [[random.randrange(10, 99) for y in range(c1)] for x in range(r1)]
            # print(matrix)  # --> [[xx, xx, ...], [xx, xx, ...], ...]
            print(s6)
            for i in range(r1):
                print(matrix[i])
            matrix0 = [[0 for j1 in range(r1)] for i1 in range(c1)]
            print(s7)
            # print(matrix0)  # перевернутая пустая матрица

    def transpose():
        for i2 in range(r1):
            for j2 in range(c1):
                matrix0[j2][r1-1-i2] = matrix[i2][j2]
        for m in matrix0:
            print(m)

    transpose()

except ValueError:
    print(s8)

except NameError:
    print(s8)
