#  s1=  -середина строки
#  s1=  middle of the line
#  s2=  -Если вы хотите увидеть середину слова или предложения
#  s2=  If you want to see the middle of a word or sentence
#  s3=  -введите текст
#  s3=  enter text
#  s4=  -в средине набранного вами текста находится "ХХХ"
#  s4=  in the middle of the text you typed is "xxx"

s1 = """
middle of the line
"""
s2 = "if you want to see the middle of a word or sentence"
s3 = "enter text:_"
print(s1.upper())
print(s2.capitalize())
a = input(s3)
b = len(a)
c = int(b)
if(c%2 == 0):
    d = c/2
    e = int(d)
    f = d-1
    g = int(f)
    print(f"In the middle of the text you typed is '{a[g]}"+f"{a[e]}'")
else:
    h = (c+1)/2
    i = h-1
    j = int(i)
    print(f"In the middle of the text you typed is '{a[j]}'")
