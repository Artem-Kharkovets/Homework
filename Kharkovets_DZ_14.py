# st1= -Сумма элементов с парным индексом из двух списков.
# st2= -Даны два списка s1 и s2 одинакового размера, состоящих только из
#       чисел int/float. Создать третий список s3, содержащий сумму
#       соответствующих элементов списков s1 и s2 с одинаковым парным индексом.
#       Вывести список s3 на экран в одну строчку.
# st3= -Результат

st1 = """
    Sum of elements with paired index from two lists."""
st2 = """
Given two lists s1 and s2 of the same size, consisting only 
of integers/floats. Create a third list s3 containing the sum of
the corresponding elements of the lists s1 and s2 with the same 
pairwise index. Print the list s3 to the screen in one line.
    """
s1 = [1, 2, 3, 4, 5]
s2 = [4, 5, 6, 7, 8]
s3 = []
st3 = """
Result:"""

print(st1.upper())
print(st2)
print("s1 =", s1)
print("s2 =", s2)

s11 = s1[::2]
s22 = s2[::2]
a1 = len(s11)
i = 0
if i <= a1:
    print(st3, end=' ')
    for a in enumerate(s11):
        b = s11[i] + s22[i]
        s3.append(b)
        print(f"{s11[i]}+{s22[i]}", end=', ')
        i += 1
    print('\b\b')
    print("s3 =", s3)
