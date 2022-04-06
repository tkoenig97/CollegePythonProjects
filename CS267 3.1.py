# Binary Tree Class
class Node:

    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# In-Order function
def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.val)
        printInorder(root.right)


# Post-Order function
def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.val)


# Pre-Order function
def printPreorder(root):
    if root:
        print(root.val)
        printPreorder(root.left)
        printPreorder(root.right)


# Binary Tree implementation
root = Node(8)
root.left = Node(5)
root.left.left = Node(9)
root.left.right = Node(7)
root.left.right.left = Node(1)
root.left.right.right = Node(12)
root.left.right.right.left = Node(2)
root.right = Node(4)
root.right.right = Node(11)
root.right.right.left = Node(3)

# Prints the tree with Pre-Order
print("Pre-order traversal:")
printPreorder(root)

# Prints the tree with In-Order
print("\nIn-order traversal:")
printInorder(root)

# Prints the tree with Post-Order
print("\nPost-order traversal:")
printPostorder(root)