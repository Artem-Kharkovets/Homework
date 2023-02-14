#  s1= -замена символов в строке
#  s2= -Программа заменяет все вхождения буквы «h» в тексте,
#       который вы вводите, на букву «H» кроме первого и последнего вхождения.
#       Текст можно вводить со всеми грамматическими символами.
#  s3= -введите текст
#  s4= -Результат

s1 = """
    replacing characters in a string"""
s2 = """
        The program replaces all occurrences of the letter "h" in the text
        you enter with the letter "H", except for the first and last
        occurrence. Text can be entered with all grammar symbols.
     """
s3 = "enter text: "
s4 = """
        Result:"""

print(s1.upper())
print(s2)
a1 = input(s3)
a = a1.lower()  # без этой команды, если печатать в верхнем регистре,
                # то 4 раза дублируется строка и меняется только
                # последняя нужная буква или если все слова с заглавных букв,
                # то программа тоже работает не правильно

b = a.find("h")
c = a.rfind("h")
d = a.replace("h", "H")

b1 = int(b)
b2 = b1 + 1
c1 = int(c)
c2 = c1 + 1

e = d[:b1] + "h" + d[b2:]
f = e[:c1] + "h" + e[c2:]
print(s4)
print(f)
