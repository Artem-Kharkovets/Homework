# ДЗ 12. Замена символов в строке
# Дана строка. Замените в данной строке все вхождения буквы 'h' на букву 'H'
# кроме первого и последнего вхождения.
# Пример:
# "hello hill house horse" --> "hello Hill House horse"
# Подсказка: задачу можно решить без циклов, вам могут понадобиться срезы,
# методы find(), rfind(), replace()

#  s1= -замена символов в строке
#  s1=  replacing characters in a string
#  s2= -Программа заменяет в веденном вами тексте все вхождения
#       буквы 'h' на букву 'H', кроме первого и последнего вхождения.
#       также вы можете выбрать любую другую букву алфавита,
#       Программа заменит буквы нижнего регистра на верхний.
#       Текст можно вводить со всеми грамматическими знаками.
#  s2=  The program replaces all occurrences of the letter 'h' in the text you enter with the letter 'H', except for the first and last occurrences. You can also choose any other letter of the alphabet. The program will replace lowercase letters with uppercase ones. Text can be entered with all grammatical characters.
#  s3= -введите текст
#  s3=  enter text
#  s4= -для запуска программы выберите действие:
#  s4=  To launch the program, select an action:
#  s5= -для буквы 'h' нажмите клавишу 'enter' или введите нужную букву
#  s5=  for the letter "h" press the "enter" key or enter the desired letter
#  s6= -В программе нельзя вводить числа. Попробуйте еще раз!
#  s6=

s1 = """
    replacing characters in a string"""
s2 = """
    The program replaces all occurrences of the letter 'h' in
    the text you enter with the letter 'H', except for the first and 
    last occurrences. You can also choose any other letter of the alphabet.
    The program will replace lowercase letters with uppercase ones.
    Text can be entered with all grammatical characters.
      """
s3 = "enter text: "
s4 = """
    To launch the program, select an action:"""
s5 = "for the letter 'h' press the 'enter' key or enter the desired letter:_"

print(s1.upper())
print(s2)
a = input(s3)
b = a.lower

