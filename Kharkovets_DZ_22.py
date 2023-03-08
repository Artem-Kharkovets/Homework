# ДЗ 22. Переворот строки рекурсивно и в цикле.
#
# s1 = Переворот строки рекурсивно и в цикле.
# s2 = Введенный вами текст будет изменен с помощью двух функций,
# принимающих на вход строку, выполняющих переворот строки и
# возвращающих перевернутую строку.
# txt1 = введите текст
# s3 = результат
# s4 = рекурсивная функция
# s5 = обычная функция, без использования срезов и 'reversed'

s1 = "\t\tReverse string recursively and in a loop.\r"
s2 = """
    The text you enter will be modified using two functions that take a string 
    as input, reverse the string, and return the reversed string.
    """
txt1 = "Enter text: "
s3 = "\nResult:"
s4 = "\tRecursive function:"
s5 = "\tnormal function, no slices and 'reversed':"

print(s1.upper())
print(s2)
t1 = input(txt1)
print(s3)

def recursiv(x):
    if len(x) == 0:
        r1 = ""     # если в строке нет символов, то возвращает None
        return r1
    else:       # переворачиваем строку, прибавляем последний элемент строки
        result = recursiv(x[:-1])  # вызываем эту же функцию с посл. символом
        result = x[-1] + result  # прибавляем к последн. элементу нов. список
        return result

print(s4, f'{recursiv(t1):>33}')

def cycle(y):
    ccl = ""
    for n in y:
        ccl = n + ccl
    return ccl

print(s5, f'{cycle(t1):>10}')
