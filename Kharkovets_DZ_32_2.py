# ДЗ 32. Односвязный список
#
# Задача: Модифицировать класс LinkedList, который реализует односвязный
# список, добавив метод __str__ для отображения списка в удобном формате и
# insert_by_index, вставляющий элемент по указанному индексу.
#
# Цель: Научиться реализовывать методы работы с односвязными списками в Python.
#
# Односвязный список - это структура данных, состоящая из элементов,
# называемых узлами. Каждый узел содержит два поля: одно для хранения
# данных и другое – ссылку на следующий узел в списке. Последний узел
# списка имеет ссылку на None, что означает конец списка.
#
# Примеры: Вот пример односвязного списка с целыми числами:
# 1 -> 2 -> 3 -> 4 -> None
#
# Требования:
#
# Добавьте метод __str__ в класс LinkedList, который возвращает
# отформатированную строку с элементами списка.
# Например, для списка с целыми числами метод должен возвращать строчку
# в формате: "1 -> 2 -> 3 -> 4 -> None".
#
# Реализуйте метод insert_by_index(self, index, data) в классе LinkedList,
# который вставляет новый узел со значением data на позицию, определенную
# индексом index. Если индекс выходит за пределы списка, вставьте узел на
# конец списка. Учтите случай, когда список сначала пуст.


class Node:
    def __init__(self, data):            # значение и ссылка на следующий узел
        self.data = data
        self.next = None


class LinkedList:                                # создаём начало списка узлов
    def __init__(self):
        self.head = None                              # изначально список пуст

    def append(self, data):                           # добавление нового узла
        new_node = Node(data)                                     # новый узел
        if not self.head:                    # если не является началом списка
            self.head = new_node                # приравнивается к новому узлу
            return
        curr_node = self.head  # текущий узел приравниваем к начальному списку
        while curr_node.next:                       # пока есть следующий узел
            curr_node = curr_node.next         # присваиваем к следующему узлу
        curr_node.next = new_node   # = False, создаём нов.узел в конце списка

    def __str__(self):
        str1 = " "
        node = self.head
        if node != None:
            str1 += str(node.data)
            node = node.next
            while node:
                str1 += " -> " + str(node.data)
                node = node.next
        str1 += " -> None"
        return str1

    def insert_by_index(self, index, data):               # вставка по индексу
        if index == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return
        i = 1
        n = self.head
        while i < index and n is not None:
            n = n.next
            i += 1
        if n is None:
            self.append(data)
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)

    print(linked_list)  # Виведе: 1 -> 2 -> 3 -> 4 -> None

    linked_list.insert_by_index(2, 5)
    print(linked_list)  # Виведе: 1 -> 2 -> 5 -> 3 -> 4 -> None

    linked_list.insert_by_index(0, 6)
    print(linked_list)  # Виведе: 6 -> 1 -> 2 -> 5 -> 3 -> 4 -> None

    linked_list.insert_by_index(100, 7)
    print(linked_list)  # Виведе: 6 -> 1 -> 2 -> 5 -> 3 -> 4 -> 7 -> None
