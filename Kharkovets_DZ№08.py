s1 = """
palindrome words
"""                #  слова палиндромы
s2 = "to find out if a word is a palindrome"  #  чтобы узнать,
# является ли слово палиндромом
s3 = "enter a word:_"   # введите слово
s4 = """
Text must be composed of letters
 RESTART THE PROGRAM!"""
#  текст должен состоять из букв, ПЕРЕЗАПУСТИТЕ ПРОГРАММУ!
print(s1.upper())
print(s2.capitalize())
print("")
a = input(s3)
print("")
if(a.isalpha()):
    b = a.lower()
    c = b[::-1]
    if(c == b):
        print("\""+a+"\" is palindrome")
    else:
        print("\""+a+"\" is NOT palindrom")
else:
    print(s4)