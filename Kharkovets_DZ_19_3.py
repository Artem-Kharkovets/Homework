# ДЗ 19. Самый старый фильм - словарь.
#
# s1 = самый старый фильм - словарь
# s2 = Дана строка с названиями фильмов и датами их выхода на экран:
# s3 = Строку изменять нельзя.
# s4 = Вывести имя старейшего фильма на экран.
# s5 = результат

s1 = "\noldest film - dictionary"
s2 = "\nGiven a string with movie titles and release dates:\n"
s3 = "\nThe line cannot be changed."
s4 = "Display the name of the oldest movie on the screen.\n"
s5 = "Result:\n"

string = "Casablanca 1942, Gone with the Wind 1939, The Godfather 2 1972, " \
         "Citizen Kane 1941, Psycho 1960."

print(s1.upper())
print(s2)
print(string)
print(s3, "\n", s4, s5)

import re

pattern = r'([\w\s]+) (\d{4})'
list1 = re.findall(pattern, string)
movies = dict(list1)


def old_film(dictionary):
    old = min(dictionary.items(), key=lambda x: x[1])  # перевод в tuple и ищем
    print(old[0])
    return old


old_film(movies)
