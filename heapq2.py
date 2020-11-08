# Write a Python program to push an item on the heap, then pop and return the smallest item from the heap.
import heapq
heap = []
heapq.heappush(heap, ('V', 3))
heapq.heappush(heap, ('V', 2))
heapq.heappush(heap, ('V', 1))
for a in heap:
	print(a)

print("\n")

# Using heappushpop push item on the heap and return the smallest item.
heapq.heappushpop(heap, ('V', 6))
for a in heap:
	print(a)

# Write a Python program to create a heapsort, pushing all values onto a heap and then popping off the smallest values one at a time.
import heapq
def heapsort(h):
    heap = []
    for value in h:
        heapq.heappush(heap, value)
    return [heapq.heappop(heap) for i in range(len(heap))]

print(heapsort([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100]))

# Output: [10, 20, 20, 40, 50, 50, 60, 70, 80, 90, 100] 
