# Heapify method rearranges the elements of an array where the left and right sub-tree of ith element obeys the heap property.
# MAX heap
def heapify(A, n, i):
   largest = i # largest value
   l = 2 * i + 1 # left
   r = 2 * i + 2 # right
   # if left child exists
   if l < n and A[i] < A[l]:
      largest = l
   # if right child exits
   if r < n and A[largest] < A[r]:
      largest = r
   # root
   if largest != i:
      A[i],A[largest] = A[largest],A[i]
      heapify(A, n, largest)
      
# sort
def heapSort(A):
   n = len(A)
   # maxheap
   for i in range(n, -1, -1):
      heapify(A, n, i)
   # element extraction
   for i in range(n-1, 0, -1):
      A[i], A[0] = A[0], A[i] # swap
      heapify(A, i, 0)
# main
A = [22,33,4,5,66,7,8,99]
heapSort(A)
for i in range(len(A)):
   print (A[i],end=" ")
