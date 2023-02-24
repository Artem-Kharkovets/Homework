# s1 = соседи
# s2 = Сформировать кортеж из целых чисел путём генерации 10 случайных чисел.
#  Найти сколько в этом кортеже элементов, которые больше двух своих соседей.
#  Крайние элементы кортежа не учитывать, поскольку у них недостаточно соседей.
# s4 =  Количество элементов, больше своих соседей =

s1 = """
        neighbours
        """
s2 = """    Form a tuple of integers by generating 10 random numbers.
    Find how many elements in this tuple that are greater than two of
    their neighbors. The extreme elements of the tuple are not taken
    into account, since they do not have enough neighbors.
    """
s3 = "Result:"
s4 = "Number of elements greater than its neighbors ="
print(s1.upper())
print(s2)

import random

t1 = []
i = 0  # общее количества чисел
b = 0  # количество наибольших чисел по сравнению с соседями

while i < 10:
    i += 1
    a = random.randint(0, 1000)
    t1.append(a)

for n in range(1, len(t1)-1):
    if t1[n - 1] < t1[n] > t1[n + 1]:
        b += 1

t2 = tuple(t1)
print(s3)
print(t2)
print(s4, b)
