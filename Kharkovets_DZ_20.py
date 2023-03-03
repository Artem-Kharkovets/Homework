# s1 = List Comprehension Фильтрация списка
# s2 = Дан список строк:
# s3 = С помощью 'list comprehension' создать новый список, содержащий только
#      строки длиннее 4 символов. Строчки в новом списке должны быть в верхнем
#      регистре.

s1 = "\n\t\tList comprehensions - Filtering lists\n"
s2 = "\tGiven a list of strings 'list1':\n\n"
list1 = ['apple', 'banana', 'cherry', 'date']
s3 = """\n
   With 'list comprehension' create a new list containing only strings 
   longer than 4 characters. The strings in the new list must be in upper case.
     """
s4 = "Result: "

print(s1.upper())
print(s2, list1, s3)

l = [n.upper() for n in list1 if len(n) > 4]
print(s4, l)
