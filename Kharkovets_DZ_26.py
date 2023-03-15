# ДЗ 26. Подсчитать количество вхождений каждого слова в файле.

# s1 = Подсчет количества вхождений каждого слова в файле.
# s2 = Создать скрипт, читающий текст из файла lorem.txt и подсчитывающий
#      количество вхождений каждого слова в тексте. Результат вывести в
#      файл stats.txt, где в каждом строке записано слово из текста без
#      повторений и количество его вхождений в файле: "<слово>: <число>".

s1 = "\n\t\tCount the number of occurrences of each word in the file.\n"
s2 = """
    Create a script that reads text from lorem.txt and counts the number of 
    occurrences of each word in the text. Output the result to 
    the stats.txt file, where each line contains a word from the text without 
    repetitions and the number of its occurrences 
    in the file: '<word>: <number>'.
    """
txt1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur " \
       "eget viverra nisi. Integer ut purus vitae odio varius mattis. " \
       "Aliquam risus tortor, consectetur et eleifend eget, congue in " \
       "lectus. Maecenas dolor elit, auctor pulvinar convallis vel, " \
       "posuere et quam. Maecenas in dolor pharetra, blandit tellus " \
       "eget, maximus mi. Fusce vitae lectus at felis imperdiet faucibus " \
       "non et odio. Aliquam et sodales orci. Phasellus nec augue id " \
       "augue ultricies posuere. Morbi porttitor sem quis nisi facilisis " \
       "fermentum. Phasellus rutrum nisl diam, vitae porta nibh ultricies " \
       "tristique. Suspendisse egestas, sapien eget finibus auctor, arcu " \
       "odio consequat leo, eget mattis mauris nisi eu nulla. Aliquam " \
       "placerat lacus at mi condimentum, a dictum tellus pretium. Vivamus " \
       "commodo turpis non sem ornare gravida. Suspendisse sed justo nec " \
       "libero semper dapibus. Vestibulum ullamcorper id metus vitae " \
       "pretium. Etiam nec placerat odio."

import re

print(s1.upper(), s2)

f = open('lorem.txt', 'w')
f.write(txt1)
f.close()

dict1 = {}
file = open('lorem.txt', 'r')
d1 = file.read().lower()
#print('d1: ', type(d1), d1)

d2 = re.sub(r'[^\w\s]', '', d1)
#print('d2: ', type(d2), d2)

d3 = d2.split()
#print('d3: ', type(d3), d3)

for words in d3:
       if words in dict1:
              dict1[words] += 1
       else:
              dict1[words] = 1
#print(type(dict1), dict1)

with open('stats.txt', 'w') as record:
       for key, meaning in dict1.items():
              record.write('{}:{}\n'.format(key, meaning))
