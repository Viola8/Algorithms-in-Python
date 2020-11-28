from queue import Queue

# Initializing a queue
q = Queue(maxsize = 3)

# qsize() give the maxsize of the Queue
print(q.qsize())  # 0

# Adding of element to queue
q.put('a')
q.put('b')
q.put('c')

# Return Boolean for Full Queue
print("\nFull: ", q.full()) # True

# Removing element from queue
print(q.get()) # a
print(q.get()) # b
print(q.get()) # c

# Return Boolean for Empty Queue
print("\nEmpty: ", q.empty()) # True

q.put(1)
print("\nEmpty: ", q.empty()) # False
print("Full: ", q.full()) # False
