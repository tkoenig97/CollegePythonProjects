class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


root = Node("0003")
root.left = Node("0002")
root.right = Node("0004")
root.right.right = Node("0006")
root.right.right.left = Node("0005")
root.right.right.right = Node("0010")

print(root.val)
print(root.right.val)
print(root.right.right.val)
print(root.right.right.right.val)