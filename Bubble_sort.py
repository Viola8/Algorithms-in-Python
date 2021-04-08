 def bubble_sort(A):
     N = len(A)
     for bypass in range(1,N):
         for k in range(0, N-bypass):
             if A[k] > A[k+1]:
                 A[k],A[k+1] = A[k+1],A[k]
    return A
print(bubble_sort(34,6,78,12,5,1,9))
