class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.val),
        printInorder(root.right)


def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.val),


def printPreorder(root):
    if root:
        print(root.val),
        printPreorder(root.left)
        printPreorder(root.right)


root = Node("0100")
root.left = Node("0060")
root.right = Node("0110")
root.left.left = Node("0050")
root.left.right = Node("0067")
root.right.left = Node("0109")
root.right.right = Node("0111")

print("In-order: ")
printInorder(root)
print("Pre-order: ")
printPreorder(root)
print("Post-order: ")
printPostorder(root)
