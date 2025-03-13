class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Добавление элемента на вершину стека"""
        self.items.append(item)

    def pop(self):
        """Удаление и возврат элемента с вершины стека"""
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        """Просмотр верхнего элемента без удаления"""
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        """Проверка на пустоту"""
        return len(self.items) == 0

    def size(self):
        """Размер стека"""
        return len(self.items)


s = Stack()
s.push(1)
s.push(2)
print('Стек')
print(s.pop())  # 2
print(s.peek())  # 1


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Добавление элемента в конец очереди"""
        self.items.append(item)

    def dequeue(self):
        """Удаление и возврат элемента из начала очереди"""
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def front(self):
        """Просмотр первого элемента без удаления"""
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
        """Проверка на пустоту"""
        return len(self.items) == 0

    def size(self):
        """Размер очереди"""
        return len(self.items)


# Пример использования
q = Queue()
q.enqueue(1)
q.enqueue(2)
print('Очередь')
print(q.dequeue())  # 1
print(q.front())  # 2