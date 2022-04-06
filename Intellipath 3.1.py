class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


bookID1 = 1000
bookID2 = 2000
bookID3 = 3000
bookID4 = 4000

s = Stack()

s.push(bookID1)
s.push(bookID2)
s.push(bookID3)
s.push(bookID4)
print("Size after pushing: " + str(s.size()))

s.pop()
s.pop()
s.pop()
s.pop()
print("Size after popping: " + str(s.size()))