class Stack:
    def __init__(self):
        self.data = []

    def push(self, v):
        self.data.append(v)

    def peek(self):
        return self.data[-1]

    def pop(self):
        return self.data.pop()

    def length(self):
        return len(self.data)

    def clear(self):
        self.data.clear()


s = Stack()
s.push(10)
s.push(20)
print(s.pop())
