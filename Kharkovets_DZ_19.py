# ДЗ 19. Самый старый фильм - словарь
# Дана строка с названиями фильмов и датами их выхода на экран: "Casablanca 1942, Gone with the Wind 1939, The Godfather 1972, Psycho 1960". Строку изменять нельзя.
# Превратить данную строку в словарь, где ключи это имена фильмов, а значение – год выхода.
#
# movies = {
#    'Casablanca': 1942,
#    'Gone with the Wind': 1939,
#    'The Godfather': 1972,
#    'Citizen Kane': 1941,
#    'Psycho': 1960
#  }
#
# Написать функцию, которая принимает на вход словарь с фильмами и возвращает имя старейшего фильма с помощью оператора return.
# Вывести имя старейшего фильма на экран.
#
# Результат: 'Gone with the Wind'
#
# Подсказка: вам могут понадобиться split и rsplit

# s1 = самый старый фильм - словарь
# s2 = Дана строка с названиями фильмов и датами их выхода на экран:
# s3 = Строку изменять нельзя.
# s4 = Вывести имя старейшего фильма на экран.
# s5 = результат

s1 = "\noldest film - dictionary"
s2 = "\nGiven a string with movie titles and release dates:\n"
s3 = "\nThe line cannot be changed."
s4 = "Display the name of the oldest movie on the screen.\n"
s5 = "Result:"

ms = """    Casablanca 1942, Gone with the Wind 1939, The Godfather 1972, 
    Citizen Kane 1941, Psycho 1960."""

print(s1.upper())
print(s2)
print(ms)
print(s3, "\n", s4, "\n", s5)

