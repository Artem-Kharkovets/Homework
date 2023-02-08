
#                           ***
# До нашей эры года высчитываются точно также, поэтому я не вводил
# обратный отсчет, со знаком "минус"
#                           ***

#  s1= -Годы и века
#  s1=  years and centuries
#  s2= -Как узнать к какому столетию относится тот или иной год? Все просто
#  s2=  How do you know which century a year belongs to? Everything is simple
#  s3= -введите интересующий вас год
#  s3=  enter the year you are interested in
#  s4= -Нет нулевого года. После окончания 1 г. до н.э.  начинается 1 год нашей эры
#  s4=  There is no zero year. After the end of 1 BC. 1 AD begins
#  s5= -вводите только числа, ПЕРЕЗАПУСТИТЕ ПРОГРАММУ!
#  s5=  Enter only numbers, RESTART THE PROGRAM!
#  s6= -XXX год относится к ZZZ веку
#  s6=  The year XXX belongs to the ZZZst century.
#  начальное столетие
#  initial century
s1 = """
years and centuries
"""
s2 = """How do you know which century a year belongs to? Everything is simple
"""
s3 = "enter the year you are interested in:_"
s4 = """There is no zero year. After the end of 1 BC. 1 AD begins
RESTART THE PROGRAM!"""
s5 = """
Enter only numbers, RESTART THE PROGRAM!"""
print(s1.upper())
print(s2)
a = input(s3)
if(a.isdigit()):
    year = int(a)
    if(year == 0):
        print(s4)
    else:
        if(101>year>0):
            century = 1
            print(f"The year {year} belongs to the {century}st century.")
        else:
            initialcentury = year % 100
            if(initialcentury == 0):
                century = int(year/100)
                print(f"The year {year} belongs to the {century}st century.")
            else:
                century = ((year-initialcentury)//100)+1
                print(f"The year {year} belongs to the {century}st century.")
else:
    print(s5)
