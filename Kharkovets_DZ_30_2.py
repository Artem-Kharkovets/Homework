# ДЗ 30. Буферизированный вывод в файл
#
# s1 - Буферизированный вывод в файл
# s2 - Написать класс, обеспечивающий буферизированный вывод в файл, где
#     каждые 5 символов хранятся в буфере и переносятся в файл. При закрытии
#     класса без функции 'close' остаток буфера записывается в файл.


s1 = "\n\t\tBuffered output to file\n"
s2 = """
    Write a class that provides buffered output to a file, where every 
    5 characters are stored in a buffer and transferred to a file. 
    When a class is closed without the 'close' function, the remainder of 
    the buffer is written to the file.
    """


class Buffered:

    def __init__(self, file_name):
        self._filename = file_name
        self.f = open(self._filename, 'w')
        self.temp = ""

    def write(self, text):
        self.temp += text
        while len(self.temp) >= 5:
            self.f.write(self.temp[:5])
            self.temp = self.temp[5:]

    def close(self):
        if self.temp:
            self.f.write(self.temp)
            self.f.close()
        else:
            self.f.close()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


print(s1.upper(), s2)


# Создаем экземпляр класса и открываем файл на запись
buffered_file = Buffered("output.txt")

# Добавляем текст в буфер
buffered_file.write("Hell")
# В файле ничего не записано; в буфере остается текст "Hell"

# Добавляем текст в буфер
buffered_file.write("o, world!")
# В файл записано "Hello, wor"; в буфере остается текст "ld!"

# Добавляем текст в буфер
buffered_file.write(" Hello Python!")
# В файл записано "Hello, world! Hello Pytho"; в буфере остается текст "n!"

# Закрываем файл
buffered_file.close()
# В файл записано "Hello, world! Hello Python!"
