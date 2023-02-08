#    ***    англійську ще не знаю, тому користуюсь гугл перекладачем   ***
# ця програма дозволяє підрахувати кількість голосних у рядку
s1 = """this program allows you to count the number of vowels in a line"""
# введіть текст
s2 = "enter text: "
print(s1.capitalize())
s3 = input(s2)
s4 = s3.upper()
s5 = (s4.count('A'))
s6 = (s4.count('E'))
s7 = (s4.count('I'))
s8 = (s4.count('O'))
s9 = (s4.count('U'))
s10 = (s4.count('Y'))
s11 = s5+s6+s7+s8+s9+s10
# у цьому тексті ХХХ голосних
print("in this text there are ", s11, " vowels")
