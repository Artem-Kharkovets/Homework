# s1 = Функция подсчета слов
# s2 = Дан список слов:
# s3 = Вывести на экран список строк, начинающихся с гласной буквы и количество строк, начинающихся с согласных букв.

s1 = "\n\t\tWord count function\n"
s2 = "\n\tGiven a list of words."
list1 = ['apple', 'banana', 'cherry', 'date', 'ananas']
s3 = """
    Show a list of lines that start with a vowel and the number of lines 
    that start with a consonant."""
s4 = "\nResult:"

print(s1.upper(), s2, s3, s4)

def tuple():
    vowel = "aeiouy"
    list2vowel = []
    list3 = ()
    for n1 in list1:
        for n2 in vowel:
            if n2 == n1[0]:
                list2vowel.append(n1)
    consonants = int(len(list1)-len(list2vowel))
    list3 = list2vowel, consonants
    return list3

print(list1, "-->", tuple())
