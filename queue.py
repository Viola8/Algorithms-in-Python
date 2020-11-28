# FIFO = first in first out LILO = last in last out
class Queue:

  def __init__(self):
      self.queue = list()

  def addtoq(self,dataval):
# Insert method to add element
      if dataval not in self.queue:
          self.queue.insert(0,dataval)
          return True
      return False

  def size(self):
      return len(self.queue)
# Pop method to remove element
  def removefromq(self):
      if len(self.queue)>0:
          return self.queue.pop()
      return ("No elements in Queue!")

TheQueue = Queue() # the queue objest is defined
TheQueue.addtoq("a")
TheQueue.addtoq("b")
TheQueue.addtoq("c")
print(TheQueue.size()) # 3
print(TheQueue.removefromq()) # a
print(TheQueue.removefromq()) # b
print(TheQueue.removefromq()) # c
print(TheQueue.removefromq()) # No elements in Queue!

# 2
queue = []  # Initializing a queue

# Adding elements to the queue
queue.append('a')
queue.append('b')
queue.append('c')

print(queue)  # ['a','b','c'] initial queue

# Removing elements from the queue
print("\nElements dequeued from queue")
print(queue.pop(0)) # a
print(queue.pop(0)) # b
print(queue.pop(0)) # c

print("\nQueue after removing elements")
print(queue) # []
