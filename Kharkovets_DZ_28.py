# ДЗ 28. Конвертировать JSON в CSV.
#
# s1 - Конвертация JSON в CSV.
# s2 - Дан файл clients.json с данными клиентов. Прочитать файл client.json с
#      помощью модуля 'json'. После импорта это будет список словарей в Python.
#      Изменить прочитанный JSON таким образом, чтобы записать его в файл CSV с
#      помощью модуля 'csv'. Ключи словарей должны быть названиями колонок.
# s3 - Читаем файл clients.json и выводим его на экран:
# s4 -

import json
import csv


s1 = "\n\t\tJSON to CSV conversion.\n"
s2 = """
    Given a client.json file with client statistics. Read client.json file 
    with using the 'json' module. Once imported, this will be a list of 
    dictionaries in Python. Modify the read JSON in such a way as to save 
    it to a CSV file with using the 'csv' module. Dictionary keys must be 
    column names.
     """
s3 = "\n\tRead the client.json file and print it to the screen:\n"


print(s1.upper(), s2, s3)

with open('clients.json') as f:
    clients_dict = json.load(f)

for a in clients_dict:
    print(a)

cols = []


for b in clients_dict:
    for key in b.keys():
        if key in cols:    # перебираем уникальные значения столбцов, не меняя
            continue       # последовательности, иначе можно сделать через set
        else:
            cols.append(key)

print("Top row:", cols)

with open("table.csv", "w", newline='') as f1:
    header = cols
    writer = csv.DictWriter(f1, fieldnames=header)

    writer.writeheader()

    for line in clients_dict:
        writer.writerow(line)
