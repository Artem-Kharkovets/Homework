# s1 = Функция подсчета слов
# s2 = Дан список слов:
# s3 = Вывести на экран список строк, начинающихся с гласной буквы и количество строк, начинающихся с согласных букв.
# s5 = список слов начинающихся с гласных
# s6 = количество слов начинающихся с согласных

s1 = "\n\t\tWord count function\n"
s2 = "\n\tGiven a list of words:\n\n"
list1 = ['apple', 'banana', 'cherry', 'date', 'ananas']
s3 = """\n
    Show a list of lines that start with a vowel and the number of lines 
    that start with a consonant."""
s4 = "\nResult:"
s5 = "\tlist of words starting with vowels:"
s6 = "\tnumber of words starting with consonants:"

print(s1.upper(), s2, list1, s3, s4)

def tuple():
    consonants = 0
    vowel = "aeiouy"
    list2vowel = []
    list3 = ()
    for n in list1:
        for n2 in vowel:
            if n2 == n[0]:
                list2vowel.append(n)
            else:
                consonants += 1
        list3 = list2vowel, consonants
    print(s5, f"\t\t{list3[0]};\n", s6, f"\t\t{list3[1]}")  # так же можно
                                                            # print(*list3)
tuple()
