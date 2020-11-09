# A stack is a linear data structure that stores items in a Last in / First out (LIFO) or First-In/Last-Out (FILO) manner.

# STACK for LIST with CLASSES:
class Stack():
    def __init__(self):
        self.items = [] # defining a class variable items
    def push(self, item): # push item
        self.items.append(item)
    def pop(self):
        return self.items.pop() # this will remove the top element of the Stack
    def is_empty(self):
        return self.items == []
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    def get_stack(self):
        return self.items # thi will retunr the items list which is the stack object
s = Stack() # the stack objest is defined
print(s.is_empty())  # True since the list is empty
s.push("A")
s.push("B")
print(s.get_stack()) # ['A','B'] A is at the bottom of the stack and B is on the top
s.push("C")
print(s.get_stack()) # ['A','B','C'] C is on the top of the stack. The element removes from the end only!!!
s.pop()
print(s.get_stack()) # ['A','B']
s.push("C")
s.push("D")
print(s.get_stack()) # ['A','B','C','D']
print(s.peek()) # D
