
from collections import deque

q = deque() # Initializing a queue

# Adding elements to a queue
q.append('a')
q.append('b')
q.append('c')

print(q) # deque(['a', 'b', 'c'])

# Removing elements from a queue
print("\nElements dequeued from the queue")
print(q.popleft()) # a
print(q.popleft()) # b
print(q.popleft()) # c

print("\nQueue after removing elements")
print(q) # deque([])
