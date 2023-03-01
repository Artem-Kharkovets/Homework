# s1 = Судоку
# s2 = Дана матрица Судоку заданная в виде одномерного списка m с 81 элементами.
# s3 = 1. Вывести на экран первую и последнюю строчку из 9 элементов в виде
#     одномерного списка.
#     2. Вывести на экран первый и последний столбец из 9 элементов в виде
#     одномерного списка.
#     3. Вывести на экран первый и последний квадрат из 9 элементов в виде
#     одномерного списка.
# s5 = Первая и последняя строка
# s6 = Первый и последний столбец
# s7 = Первый и последний квадрат

s1 = "\nSudoku"
s2 = """
Given a Sudoku matrix in the form of a one-dimensional list 'm' of 81 elements.
    """
s3 = """
1. Display the first and last line of 9 items as a one-dimensional list.
2. Display the first and last column of 9 items as a one-dimensional list.
3. Display the first and last square of 9 elements as a one-dimensional list.
    """
s4 = "Result."
s5 = "First and last line:"
s6 = "First and last column:"
s7 = "First and last square:"

m = [1, 7, 9, 3, 2, 8, 5, 6, 4,
     4, 3, 8, 6, 5, 9, 1, 7, 2,
     2, 5, 6, 7, 1, 4, 3, 8, 9,
     3, 2, 4, 8, 9, 1, 7, 5, 6,
     7, 9, 5, 4, 3, 6, 2, 1, 8,
     8, 6, 1, 2, 7, 5, 9, 4, 3,
     5, 8, 2, 1, 4, 3, 6, 9, 7,
     9, 4, 7, 5, 6, 2, 8, 3, 1,
     6, 1, 3, 9, 8, 7, 4, 2, 5]

print(s1.upper())
print(s2)

l1 = []
m1 = [l1] * 9
l = []
m2 = [l] * 9
sudoku = []           # [[], [], [], [], [], [], [], [], []]

a = 0  # элемент, с которого начинается отсчёт
b = 9  # количество строк
c = 9  # количество элементов в строке

for n2, v in enumerate(m2):
     if n2 < c:
          l = m[a:b]
          m2.append(l)
          a += c
          b += c
          if n2 == c - 1:
               for n1 in m2:
                    if not (n1 in m1):
                         sudoku.append(n1)  # [[1, 7, 9, ......... , 4, 2, 5]]
for i in sudoku:
     for j in i:
          print(j, end='  ')
     print()

print(s3)
print(s4)
print(s5)

def get_row(x1):
     x2 = x1 - 1
     x3 = sudoku[x2]
     print(f"Line {x1}:", x3)

get_row(1)
get_row(9)

print(s6)

def get_column(y1):
     y2 = y1 - 1
     y4 = []
     for i in sudoku:
          for j in i:
               y3 = i[y2]
               if j == y3:
                    y4.append(y3)
     print(f"Column {y1}:", y4)

get_column(1)
get_column(9)

print(s7)

def get_squares(z1):
     z01 = list(m[0:3] + m[9:12] + m[18:21])
     z02 = list(m[3:6] + m[12:15] + m[21:24])
     z03 = list(m[6:9] + m[15:18] + m[24:27])
     z04 = list(m[27:30] + m[36:39] + m[45:48])
     z05 = list(m[30:33] + m[39:42] + m[48:51])
     z06 = list(m[33:36] + m[42:45] + m[51:54])
     z07 = list(m[54:57] + m[63:66] + m[72:75])
     z08 = list(m[57:60] + m[66:69] + m[75:78])
     z09 = list(m[60:63] + m[69:72] + m[78:])
     z10 = z01, z02, z03, z04, z05, z06, z07, z08, z09
     z2 = z1 - 1
     for index, value in enumerate(z10):
          if index == z2:
               print(f"squares {z1}:", value)

get_squares(1)
get_squares(9)
