# st1= -Пересечение двух списков
# st2= -Даны два списка s1 и s2.Создать список s3, в котором будут содержаться
#      только общие элементы из списков s1 и s2 без дубликатов.
#      Вывести список s3 на экран в одну строчку.
# st3= -Результат

st1 = """
        Intersection of two lists"""
st2 = """
  Two lists s1 and s2 are given. Create a list s3 that will only
  contain common elements from lists s1 and s2 without duplicates. 
  Display the list s3 on the screen in one line.
        """
s1 = [1, 2, 3, 4, 5, 'six']
s2 = [4, 5, 6, "six", 7, 8]
st3 = """
  Result:"""

print(st1.upper())
print(st2)
print("  s1 =", s1)
print("  s2 =", s2)
s3 = []

for a in s1:
    if a in s2 and a not in s3:  # <and a not in s3> в данной задаче
        s3.append(a)             #  бесполезен, но для других списков - нужен
print(st3, s3)
