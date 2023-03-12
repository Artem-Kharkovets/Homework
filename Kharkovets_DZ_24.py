# ДЗ 24. Пузырьковая сортировка
#
# s1 = Пузырьковая сортировка
# s2 = Условие:
# s3 = Сформировать список из целых чисел путём генерации 10 случайных чисел.
#      Отсортировать список с помощью пузырьковой сортировки и вывести
#      результат на экран.
# s4 = Формируем случайный список:
# s5 = Сортируем список:
# s6 = Всего в этом списке произошло перемен в количестве - N шт.

import random

s1 = "\n\t\tbubble sort\n"
s2 = "\n\tCondition:"
s3 = """
     Generate a list of integers by generating 10 random numbers. 
     Sort the list using bubble sort and display the result on the screen.
     """
s4 = "We form a random list: "
s5 = "Sort the list:"

print(s1.upper(), s2, s3)

i = 10  # общее количество чисел


def bubble_sort(n):
    f = 0
    listR = []
    for a in range(n):
        b = random.randint(0, 1000)
        listR.append(b)
    print(s4, listR)
    end = n - 1
    swapped = True
    for c in range(end):
        swapped = False
        for d in range(end - c):
            if listR[d] > listR[d+1]:
                listR[d], listR[d+1] = listR[d+1], listR[d]
                swapped = True
                f += 1
            #if swapped == False:  #<-- С этим значением считает неправильно
                #break
    print(s5, f"\t\t\t{listR}")
    print(f"\nIn total, this list has changed in quantity - {f} pc.")

bubble_sort(i)
