# 1 using while loop
def insertion_sort(A):
    for i in range (1,len(A)): # unsotred list since A[i-1] is alredy sorted
        while A[i-1]>A[i] and i>0:
            A[i],A[i-1] = A[i-1],A[i]
            i-=1
    return A
print(insertion_sort([23,4,67,8,19,53,75]))

# 2 shifts instead of swapping
def insertion_sort(A):
    for i in range (1,len(A)):
        current_number = A[i]
        k = 0
        for j in range(i-1,-2,-1):
            k=j
            if A[j] > current_number:
                A[j+1] = A[j]
            else:
                break
        A[k+1] = current_number
    return A
print(insertion_sort([23,4,67,8,19,53,75]))
