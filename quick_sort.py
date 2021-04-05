# Quick sort or Hoar sort is recursive algorithm (calls itself)

def quick_sort(A):
    if len(A) <= 1:  # terminal case
        return A
    else:
        pivot = A.pop()
    items_grater = []
    items_lower = []
    for item in A:
        if item > pivot:
            items_grater.append(item)
        else:
            items_lower.append(item)
    return quick_sort(items_lower) + [pivot] + quick_sort(items_grater)

print(quick_sort([2,4,6,1]))
