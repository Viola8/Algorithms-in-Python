# Stack implementation with collections.deque
from collections import deque # Deque (Doubly Ended Queue)

stack = []

# append() function to push an item in the stack
stack.append('a')
stack.append('b')
stack.append('c')
stack.append('a')
print(stack)   # ['a','b','c','a']

stack.insert(2,'d')
print(stack) # ['a','b','d','c','a']

print(stack.count('a')) # output is 2

stack.remove('a')  # this will remove the 1st occurense of 'a'
print(stack) # [b','d','c','a']

# pop() fucntion to remove an item from stack in LIFO order
print('\nElements poped from stack:')
print(stack.pop()) # 'a'
print(stack.pop()) # 'c'
print(stack.pop()) # 'd'

print(stack) # uncommenting print(stack.pop()) will cause an IndexError as the stack is now empty
# Output: 'b'
