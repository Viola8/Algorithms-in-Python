# The goal is to look through already sorted sequence and find the element

def binary_search(list1, item):
    begin_index = 0 # lower bound
    end_index = len(list1) - 1 # upper bound

    while begin_index <= end_index:
        mid = (begin_index + end_index) // 2
        mid_value = list1[mid]
        if mid_value == item:
            return mid
        elif item < mid_value:
            end_index = mid - 1
        else:
            begin_index = mid + 1
    return None

list1 = [33,5,8,9,56,12]
item = 8
print(binary_search(list1,item))  # output: 2
