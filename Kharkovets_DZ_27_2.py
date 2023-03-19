# ДЗ 27. Бинарный поиск
#
# s1 - Бинарный поиск
# s2 - Написать функцию, которая принимает отсортированный список в качестве
# параметра и возвращает индекс найденного элемента или -1, если элемент
# не найден.
# Вывести в консоль результат работы функции для списка из 20 элементов.
# s3 - Создаем отсортированный список из 20 случайных чисел:
# s4 - Введите число, индекс которого нужно найти:

import random

s1 = "\n\t\tBinary search\n"
s2 = """
    Write a function that takes a sorted list as
    parameter and returns the index of the element found, or -1 if the element
    not found.
    Output to the console the result of the function for a list of 20 elements.
     """
s3 = "\nCreate a sorted list of 20 random numbers:"
s4 = "\nEnter the number whose index you want to find: "
s5 = "\nResult: "
s6 = "\nInvalid parameters. Restart the program!"

print(s1.upper(), s2, s3)

sorted_list = []
for i in range(20):
    sorted_list.append(random.randrange(1, 100))
sorted_list.sort()

print(sorted_list)

key = input(s4)


def binary_search(x):
    n = int(key)
    left = 0
    right = len(x) - 1
    middle = (left + right) // 2
    while n != x[middle] and left < right:  # "<=" не нужно, так как если ->
        if n > x[middle]:         # -> left=right, то и middle=left=right, ->
            left = middle + 1     # -> а если далее при обходе цикла ->
        else:                     # -> middle != n, то такого значения нет
            right = middle - 1
        middle = (left + right) // 2
    if n == x[middle]:
        print("ID =", middle)
    else:
        print(-1)
    return n


if key.isdigit():
    print(s5)
    binary_search(sorted_list)
else:
    print(s5, s6)
