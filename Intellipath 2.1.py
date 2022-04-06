class studentNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def deleteList(self):
        current = self.head
        while current:
            prev = current.next
            del current.data
            current = prev

    def insert(self, data):
        newNode = studentNode(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def printLL(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


if __name__ == '__main__':
    llist = LinkedList()
    llist.insert("Student 1")
    llist.insert("Student 2")
    llist.insert("Student 3")
    llist.insert("Student 4")

    LinkedList.printLL(llist)

    print("Deleting linked list")
    llist.deleteList()

    print("Linked list deleted")