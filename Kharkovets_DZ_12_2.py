#  s1= -замена символов в строке
#  s2= -Программа заменяет все вхождения буквы «h» в тексте,
#       который вы вводите, на букву «H» кроме первого и последнего вхождения.
#       Текст можно вводить со всеми грамматическими символами.
#  s3= -введите текст
#  s4= -Результат
#  s5= -В тексте нет ни одной буквы "h". Попробуйте ещё!
#  s6= -В тексте одна буква "h".
#  s7= -В тексте две буквы "h".

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
s5 = "There is not a single 'h' in the text. Try again!"
s6 = """There is only one "h" in the text.
     """
s7 = """There are two letters "h" in the text.
     """

print(s1.upper())
print(s2)
a = input(s3)

a1 = a.count("h")
b = a.find("h")
b1 = int(b)
b2 = b1 + 1
c = a.rfind("h")
c1 = int(c)
c2 = c1 + 1
print(s4)

if a1 == 0:
    print(s5)
else:
    if a1 == 1:
        print(s6)
        print(a)
    else:
        if a1 == 2:
            print(s7)
            print(a)
        else:
            d = a.replace("h", "H")
            e = d[:b1] + "h" + d[b2:]
            f = e[:c1] + "h" + e[c2:]
            print(f)
