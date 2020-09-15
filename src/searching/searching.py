def linear_search(arr, target):
    i = 0
    while i < len(arr):
        if arr[i] == target:
        return True
    return -1
         



shoe = [7,8,9,1,6,3,5]
print(linear_search(shoe, 3))
# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    begin_index = 0
    end_index = len(arr) -1

    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index)//2
        midpoint_value  = arr[midpoint]
        if midpoint_value == target:
            return midpoint 
        elif target < midpoint_value:
            end_index = midpoint -1
        else:
            begin_index = midpoint + 1

    return -1  # not found

boot = [2,3,4,5,6,7,8,9]
print(binary_search(boot, 5))