# ДЗ 23. Генератор: перестановки букв в строке.
#
# s1 = Генератор: перестановка букв в строке
# s2 = С помощью функции генератора, введенный Вами текст будет выведен
# на экран в последовательности строк, содержащих все перестановки букв.
# str1 = Введите текст не превышающий 10 символов
# s4 = Введенный текст должен быть в пределах 2 - 5 знаков!
# s5 = количество неповторяющихся вариантов

import itertools

s1 = "\n\t\tGenerator: permutation of letters in a string."
s2 = """\n
    With the generator function, the text you enter will be displayed on 
    the screen in a sequence of lines containing all the permutations of 
    the letters.
    """
s3 = "\nResult:"
s4 = "The entered text must be between 2 and 10 characters! TRY AGAIN!"
s5 = "Number of non-recurring options: "

print(s1.upper(), s2)


def gen(x):
    for n in itertools.permutations(x):
        yield n


f = []
while True:
    str1 = input("Enter text up to 10 characters: ")
    s = str1
    s1 = len(s)
    if 1 < s1 < 11:
        break
    else:
        print(s4)

k = 0
for i in gen(s):
    i1 = ''.join(i)
    f.append(i1)
    k += 1

print(s3)
print(f)
print(s5, k)
