def binary_search(list, item):
    left, right = 0, len(list)-1
    while left <= right:
        middle = (left+right) // 2
        if item == list[middle]:
            return middle
        elif item < list[middle]:
            right = middle - 1
        else:
            left = middle + 1
    return -1
my_list = [1,3,5,7,9]
print(binary_search(my_list, 3), 1)
print(binary_search(my_list, -1), -1)
print(binary_search([2,7,8,9,10], 9), 3)