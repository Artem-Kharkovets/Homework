#  <<Сноски делал, чтобы самому не запутаться>>

# s1= "Подсчет слов в строке с помощью словаря"
# s2= """Дана строка, содержащая только слова из букв английского алфивита,
#     пробелы и знаки препинания '.' и ','."""
# s3= """Создать словарь, содержащий слова в виде ключей(key) не зависимо от
#     регистра символов в слове, а значениями (value) должно быть число
#     вхождений данного слова в строку."""
# s5= Словарь:
# s6= Слово, встречающееся в тексте чаще всего -


s1 = """
\t\tCount words in a string with a dictionary"""
s2 = """
Given a string containing only words from the letters of 
the English alphabet, spaces and punctuation '.' And ','."""
s3 = """Create a dictionary containing words in the form of keys (key) 
the word is case-insensitive, and the values (value) should be the 
number of occurrences of the given word in the string.
     """
a1 = "One, two, three, one, two, five. Two, five."
s4 = """
    Result:"""
s5 = "Dictionary:"
s6 = "The word that occurs most often in the text -"

print(s1.upper())
print(s2)
print(s3)
print(a1)
print(s4)

a2 = a1.lower()
a3 = a2.split(" ")
l1 = []  # ['one,', 'two,', 'three,', 'one,', 'two,', 'five.', 'two,', 'five.']

for b1 in a3:
    a5 = b1.strip(',.')
    l1.append(a5)  # ['one', 'two', 'three', 'one', 'two', 'five', 'two', ->
                   #  -> 'five'] <class 'list'>
set1 = set(l1)  # {'three', 'one', 'two', 'five'}
l2 = list(set1)  # ['five', 'three', 'one', 'two']
l3 = []

for b2 in l2:
    c = l1.count(b2)
    l3.append(c)  # [1, 2, 2, 3]
d = dict(zip(l2, l3))  # объединяем 2 списка в словарь zip-ом
                       # {'three': 1, 'one': 2, 'five': 2, 'two': 3}
d1 = d.items()  # кортежи ([('one', 2), ('two', 3), ('five', 2), ('three', 1)])
d2 = max(d1)  # ('two', 3)
d3 = d2[0]
print(s5, d)
print(s6, f"'{d3}'")
