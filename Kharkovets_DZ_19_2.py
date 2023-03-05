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

string = "Casablanca 1942, Gone with the Wind 1939, The Godfather 1972, Citizen Kane 1941, Psycho 1960."

print(s1.upper())
print(s2)
print(string)
print(s3, "\n", s4, s5)

import re

string1 = re.sub("[0-9.]", "", string)  # в строке убираем все цифры
numbers1 = re.sub("[^0-9,]", "", string)  # в строке убираем все буквы
numbers2 = numbers1.split(",")  # создаем список из дат

movies = {}
list1 = string1.split(",")  # создаём список из фильмов

list2 = []
for l1 in list1:
    list2.append(l1.strip(" "))  # обрезаем лишние пробелы

movies = dict(zip(list2, numbers2))
print("Dictionary:\n", movies)

old_film = min(movies, key=movies.get)
print(f"\n\tOldest film:\t'{old_film}'")
