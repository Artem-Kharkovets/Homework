#    ***    англійську ще не знаю, тому користуюсь гугл перекладачем   ***
# ця програма дозволяє підрахувати кількість голосних у рядку
s1 = """this program allows you to count the number of vowels in a line"""
# введіть текст
s2 = "enter text: "
print(s1.capitalize())
s3 = input(s2)
s4 = s3.lower()

s5 = (s3.count("A")+s3.count("E")+s3.count("I")+s3.count("O")+s3.count("U")+s3.count("Y")+s3.count("a")+s3.count("e")+s3.count("i")+s3.count("o")+s3.count("u")+s3.count("y"))
s6 = (s4.count("aeiouy"))
# у цьому тексті ХХХ голосних
print("in this text there are ", s4, " vowels")
print("s6: in this text there are ", s6, "vowels")
