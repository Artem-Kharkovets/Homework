#  найти середину строки
#  задача
#  1. найти середину строки
#  2. найти буквы, которые содержаться в середине предложения
#  3. ответ должен быть из одной или двух букв
#  4. если в середине предложения пробел, то вывести описание
#  "в середине текста пробел, который объединяет слова "ХХХ ХХХ и буквы XZ"
#  подсказка
#  понадобятся операторы if/else,// цельночисленное деление, % остаток от деления и срезы s[a:b]
#  Если вы хотите увидеть середину слова или предложения
#  Введите текст
print("""
If you want to see the middle of a word or sentence
""")
s1 = input("enter text:_")
a = len(s1)
b = a/2
if(int(b)):
    c = b-1
    d = s1[b]+s1[c]
    print("in the middle of your text the following characters  \'"+s1[d]+'\'') #  в середине Вашего текста находятся следующие символы
