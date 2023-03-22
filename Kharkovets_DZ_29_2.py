# ДЗ 29. Реализовать Стек
#
# s1 - Реализация стека
# s2 - Состояние стека
# s3 - Введите данные
# s4 - Добавить элемент
# s5 - Извлечь элемент
# s6 - Конец списка
# s8 - Нажмите ввод(Вызвать меню) или введите команду:
# s9 - Меню: 1 - состояние стека; 2 - проверка пустого стека;
#      3 - добавить элемент; 4 - извлечь элемент; 5 - конец списка;
#      0 - завершить программу.
# s10 - стек пустой
# s11 - недопустимый параметр

s1 = "\n\t\tStack implementation\n"
s2 = "Stack state: "
s3 = "Enter data: "
s4 = "Add element: "
s5 = "Extract element: "
s6 = "List End: "
s7 = """At night you need to drink 5-7 liters of beer - in the morning 
        a swollen face is easier to shave. The End!"""
s8 = "Press enter (Call menu) or enter the command: "
s9 = """
        Menu: 
    1 - stack state
    2 - check for an empty stack
    3 - add an element
    4 - extract the element 
    5 - end of the list
    0 - end the program
    """
s10 = "Stack empty - "
s11 = "Invalid parameter"


print(s1.upper())


class Stack:

    def __init__(self):                         # инициализация пустого списка
        self._list1 = []

    def empty(self):                              # 2 - проверка пустого стека
        if len(self._list1) == 0:
            return True

    def peek(self):                     # 5 - возвращает элемент с верха стека
        if len(self._list1) > 0:
            return self._list1[-1]

    def push(self, item):          # 3 - добавляет новый элемент на верх стека
        self._list1.append(item)
        return self._list1

    def pop(self):            # 4 - удаляет и возвращает элемент с верха стека
        if len(self._list1) > 0:
            return self._list1.pop()

    def stack_state(self):                               # 1 - состояние стека
        return self._list1


new_stacke = Stack()

a1 = None


while a1 != 0:
    a = input(s8)
    if a == "":
        print(s9)
    else:
        if not a.isdigit():
            print(s11)
        else:
            a1 = int(a)
            if not(-1 < a1 < 6):
                print(s11)
            else:
                if a1 == 0:
                    print(s7)
                    break
                if a1 == 1:
                    print(s2, new_stacke.stack_state())
                if a1 == 2:
                    print(s10, new_stacke.empty())
                if a1 == 3:
                    print(s4)
                    new_stacke.push(input(s3))
                if a1 == 4:
                    print(s5, new_stacke.pop())
                if a1 == 5:
                    print(s6, new_stacke.peek())
