#  s1=  -середина слова
#  s1=  middle of a word
#  s2= -Если вы хотите знать, что находится в середине слова
#  s2=  If you want to know what is in the middle of a word
#  s3=  -введите текст
#  s3=  enter text
#  s4= -в средине Вашего слова находится "ХХХ"
#  s4=  in the middle of your word is "xxx"
#  s5= -текст должен состоять только из букв, ПЕРЕЗАПУСТИТЕ ПРОГРАММУ!
#  s5=  The text must consist only of letters, RESTART THE PROGRAM!

s1 = """
middle of a word
"""
s2 = "if you want to know what is in the middle of a word"
s3 = "enter text:_"
print(s1.upper())
print(s2.capitalize())
a = input(s3)
if(a.isalpha()):
    b = len(a)
    c = int(b)
    if(c%2 == 0):
        d = c/2
        e = int(d)
        f = d-1
        g = int(f)
        print(f"in the middle of your word is '{a[g]}"+f"{a[e]}'")
    else:
        h = (c+1)/2
        i = h-1
        j = int(i)
        print(f"in the middle of your word is '{a[j]}'")
else:
    print("""
    The text must consist only of letters
    \t\tRESTART THE PROGRAM!""")
