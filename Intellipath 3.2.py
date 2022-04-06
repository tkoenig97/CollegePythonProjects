class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def reverse(self):
        return self.items.reverse()


q = Queue()

q.enqueue("Bonnai")
q.enqueue("Tim")
q.enqueue("Jerry")
q.enqueue("Tom")

print(q.peek())
q.reverse()
print(q.peek())