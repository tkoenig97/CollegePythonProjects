# Defining the stack
stack = []

# Displays the initial size of the stack
print("Initial size: ")
print(stack.__len__())

# Displays initial content of the stack
print('\nInitial stack: ')
print(stack)

# Pushing elements into the stack
stack.append("LCD")
stack.append("LED")
stack.append("Mobile")
stack.append("Charger")
stack.append("Speaker")
stack.append("Mouse")
stack.append("Keyboard")
stack.append("Laptop")

# Displays size after pushing
print("\nSize after pushing: ")
print(stack.__len__())

# Displays the content of the stack after pushing
print('\nStack after elements are pushed:')
print(stack)

# Popping the top 3 elements from the stack
stack.pop()
stack.pop()
stack.pop()

# Displays the size after popping
print("\nSize after popping: ")
print(stack.__len__())

# Displays the stack after popping
print('\nStack after elements are popped:')
print(stack)