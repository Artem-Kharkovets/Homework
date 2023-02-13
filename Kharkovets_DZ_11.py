# ДЗ 11. Последовательности целых чисел.
# Программа запрашивает ввод с клавиатуры целых чисел до тех пор,
# пока не будет введено 0.
# После ввода 0 необходимо вывести следующую информацию на экран:
# Количество введенных чисел (последний 0 не считается)
# Сумму введенных чисел
# Среднее арифметическое всех введенных чисел (последний 0 не считается)
# Определить минимальное и максимальное значение (последний 0 не считается)
# Определить количество четных и нечетных элементов последовательности
# (последний 0 не считается)
# Пример:
# Введите число: 1
# Введите число: 2
# Введите число: 3
# Введите число: 0
# Результат:
# Количество введенных чисел 3
# Сумма введенных чисел 6
# Среднее арифметическое всех введенных чисел 2
# Минимум 1, максимум 3
# Парных 1, нечетных 2
# Использование списков не желательно.

#  s1 -последовательности целых чисел
#  s2 -программа запрашивает ввод целых чисел, для завершения нужно ввести
#       0 (ноль). по итогу программа выводит на экран количество, сумму и
#       среднее арифметическое всех введенных чисел, минимальное и
#       максимальное значение, а также количество четных и нечетных
#       элементов последоватльности.
#  s3 -введите число
#  s4 -результат
#  s5 -количество введенных чисел
#  s6 -сумма введенных чисел
#  s7 -среднее арифметическое всех введенных чисел
#  s8 -минимум
#  s9 -максимум
#  s10 -количество четных элементов последовательности
#  s11 -количество нечетных элементов последовательности
#  s12 -Это не целое число, нужно ввести только целое число!
#  s13 -Хватит дурачится, перезапусти программу!
#  s13  Stop fooling around, restart the program!
#  s14 -два числа... серьезно??? ну ладно
#  s14  Two numbers... seriously??? OK

s1 = """
    sequences of integers"""
s2 = """
    The program asks to enter whole numbers, to complete 
    you need to enter 0 (zero). As a result, 
    the program displays the number, the sum and 
    arithmetic mean of all entered numbers, 
    the minimum and maximum values, as well as the number 
    of even and odd elements of the sequence.
     """
s3 = "enter the number: "
s4 = """
    Result:"""
s5 = "Number of entered numbers:"
s6 = "Sum of entered numbers:"
s7 = "Arithmetic mean of all entered numbers: "
s8 = "Minimum: "
s9 = "Maximum: "
s10 = "Number of even sequence elements: "
s11 = "The number of odd elements in the sequence: "
s12 = "It's not an integer, you only need to enter an integer!"
s13 = "Stop fooling around, restart the program!"
s14 = "Two numbers... seriously??? OK"

print(s1.upper())
print(s2)

input1 = 0  # количество ввода чисел
si1 = 0  # сумма введенных чисел
even1 = 0  # количество четных чисел
odd1 = 0  # количество нечетных чисел
max1 = 0
# min1 = si1  !!!!при этом значении итог будет равен нулю!!!!

while True:
    a = input(s3)
    if a.isdigit():
        a1 = int(a)
        if a1 == 0:  # если введенное число = 0, то прерывание цикла
            input1 += 0
            break
        input1 += 1
        si1 = si1 + a1
        a2 = a1
        a3 = a1
        min1 = a3  # !!!при этом значении итог = последнему введенному числу!!!
        if a2 > max1:
            max1 = a2
        if a3 < min1:
            min1 = a3
        if a1 % 2 == 0:
            even1 += 1
        if a1 % 2 != 0:
            odd1 += 1
    else:
        print(s12)
print(s4)

if input1 <= 1:
    print(s13)
else:
    if input1 == 2:
        print(s14)
        print()
        print(s5, input1)
        print(s6, si1)
        sa1 = si1 / input1  # среднее арифметическое введенных чисел
        sa2 = round(sa1, 1)
        print(s7, sa2)
        print(f"minimum: {min1}; maximum: {max1}")
        print(s10, even1)
        print(s11, odd1)
    else:
        print(s5, input1)
        print(s6, si1)
        sa1 = si1 / input1  # среднее арифметическое введенных чисел
        sa2 = round(sa1, 1)
        print(s7, sa2)
        print(f"minimum: {min1}; maximum: {max1}")
        print(s10, even1)
        print(s11, odd1)
