import heapq
list1 = [5,7,9,1,3,2,10]
heapq.heapify(list1)
print(list1) # [1,3,2,7,5,9,10]

# Inserting into heap
heapq.heappush(list1,4)
print(list1) # [1,3,2,4,5,9,10,7]

# Removing the element from the heap
print(heapq.heappop(list1)) # output: 1. This is the root element of the array.
print(list1) # [2,3,7,4,5,9,10]

# Replacing in a heap
# The heapreplace function always removes the smallest element of the heap
# and inserts the new incoming element at some place not fixed by any order.

heapq.heapreplace(list1,6)
print(list1) # [3,4,7,6,5,9,10]
