class Stack:
    def __init__(self):
        self.container = []
        self.size = 0

    def __raise_size(self):
        if self.is_empty:
            raise IndexError('Нельзя брать из пустого стэка')

    @property
    def is_empty(self):
        return self.size == 0

    @property
    def pop(self):
        self.__raise_size()
        self.size -= 1
        return self.container.pop(self.size)

    @property
    def peek(self):
        self.__raise_size()
        return self.container[-1]

    def push(self, element):
        self.size += 1
        self.container.append(element)