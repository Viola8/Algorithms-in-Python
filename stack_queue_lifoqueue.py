from queue import LifoQueue

stack = LifoQueue(maxsize = 3) # Initializing a stack

print(stack.qsize()) # qsize() show the number of elements in the stack   # Output: 0

# put() function to push element in the stack
stack.put('a')
stack.put('b')
stack.put('c')

print("Full: ", stack.full())   # Full: True
print("Size: ", stack.qsize()) # Size: 3

# get() fucntion to pop element from stack in LIFO order
print('\nElements poped from the stack')  # c b a
print(stack.get())
print(stack.get())
print(stack.get())

print("\nEmpty: ", stack.empty()) # Empty: True
