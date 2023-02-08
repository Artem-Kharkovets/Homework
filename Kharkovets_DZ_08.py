s1 = """
palindrome words
"""                #  слова палиндромы
s2 = "to find out if a word is a palindrome"  #  чтобы узнать,
# является ли слово палиндромом
s3 = "enter a word:_"   # введите слово
s4 = """
The text must consist only of letters
 RESTART THE PROGRAM!"""
#  текст должен состоять только из букв, ПЕРЕЗАПУСТИТЕ ПРОГРАММУ!
print(s1.upper())
print(s2.capitalize())
print("")
word = input(s3)
print("")
if(word.isalpha()):
    b = word.lower()
    c = b[::-1]
    if(c == b):
        print(f"'{word}' is palindrome")
    else:
        print(f"'{word}' is NOT palindrome")
else:
    print(s4)
