# ДЗ 31. Система управления библиотекой
#
# s1 = система управления библиотекой
# s2 = Задача: Создать систему для управления библиотекой с помощью
#      классов Author, Book и Library

import json

s1 = "library management system"
s2 = """
    Task: 
    Create a library management system using the Author, Book and 
    Library classes."""


class Author:
    def __init__(self, first_name: str, last_name: str, birth_date: str):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date

    def __str__(self):
        return f'first_name: {self.first_name}, ' \
               f'last_name: {self.last_name}, ' \
               f'birth_date: {self.birth_date}'


class Book:
    def __init__(self, title: str, author: Author, publication_year: int):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def __str__(self):
        return f'title: {self.title}, {self.author}, ' \
               f'publication_year: {self.publication_year}'


class Library:
    def __init__(self):
        self.libr = []

    def add_book(self, addedBook):  # добавить книгу
        self.libr.append(addedBook)
        return self.libr

    def remove_book(self, deletebook):  # удалить книгу
        if deletebook in self.libr:
            self.libr.remove(deletebook)
        return self.libr

    def __str__(self):
        for item in self.libr:
            print(f"{str(item)}")  # TypeError: __str__ returned non-string (type list)
        # return self.libr  # TypeError: __str__ returned non-string (type list)
        # return str(library)  # RecursionError: maximum recursion depth exceeded while calling a Python object

    def dump_to_json(self, name):
        with open(f"{name}", "w") as f:
            json.dump(self.libr, f)
        return self.libr


author1 = Author("Джордж", "Оруелл", "25.06.1903")
author2 = Author("Алдус", "Хаксли", "26.07.1894")

book1 = Book("Війна світів", author1, 1939)
book2 = Book("1984", author1, 1949)
book3 = Book("Красне рабство", author2, 1932)

library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print(library)
library.dump_to_json("library1.json")


