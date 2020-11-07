def selection_sort(A):
    for i in range(0,len(A)-1):
        for j in range(i+1,len(A)):
            if A[j]<A[i]:
                if j!=i:
                    A[j],A[i] = A[i],A[j]
    return A
print(selection_sort([67,15,89,3,1,8]))
