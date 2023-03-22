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
        self.file_name = file_name
        self.temp = ""

    def record(self):
        with open(self.file_name, "a") as f:  # открываем на дозапись
            f.write(self.temp)
            self.temp = ""

    def write(self, text):
        self.temp += text
        if len(self.temp) >= 5:
            self.record()

    def close(self):
        if self.temp:
            self.record()

    def __del__(self):
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
