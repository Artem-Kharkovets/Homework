#  s1 -Числа Фибоначчи.
#  s1  fibonacci numbers.
#  s2 -Программа отображает числа Фибоначчи с нужным вам количеством чисел в
#      последовательности
#  s2  The program displays the Fibonacci numbers with the number of
#      numbers you need in the sequence
#  s3 -Переменная "н" является количеством чисел в последовательности
#  s3  The variable "n" is the number of numbers in the sequence
#  s4 -Введите переменную:
#  s4  Enter a variable:
#  s5  n =
#  s6 -Вы ввели НЕ натуральное число, перезапустите программу!
#  s6  You have entered NOT a natural number, restart the program!
#  s7 -результат:
#  s7  result:
#  s8 -ряд фибоначчи для числа 'n'
#  s8  Fibonacci series for number 'n'
#  s9 -Для нуля нет результатов, перезапустите программу!
#  s9  No results for null, restart the program!

s1 = """
fibonacci numbers."""
s2 = """    
    The program displays the Fibonacci numbers with
    the number of numbers you need in the sequence.
    The variable \"n\" is the number of numbers in the sequence.
    Enter a variable:"""
s3 = "The variable \"n\" is the number of numbers in the sequence."
s4 = "Enter a variable:"
s6 = "You have entered NOT a natural number, restart the program!"
s7 = """
    Result:"""
s9 = "No results for null, restart the program!"

print(s1.upper())
print(s2 +"\n"+ s3 +"\n"+ s4)
n = input("n = ")

i = 1
x1 = 0
x2 = 1

if n.isdigit():
    n1 = int(n)
    print(s7)
    print(f"Fibonacci numbers for \'{n}\':")
    if n1 == 0:
        print(s9)
    else:
        if n1 == 1:
            print(x1)
        else:
            if n1 == 2:
                print(f"{x1}, {x2}.")
            else:
                s8 =(f"{x1}, {x2}")
                print(s8, end=', ')
                i = 2
                while n1 > i:
                    x3 = x1 + x2
                    x1 = x2
                    x2 = x3
                    n1 -= 1
                    print(x2, end=', ')
else:
    print(s6)
