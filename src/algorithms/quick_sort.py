import random

arr = [1,2,3,7,4,5,6]
def sum (arr):
    if len(arr) == 1:
        return arr[0]
    return arr[0] + sum(arr[1:])
# print(sum(arr))

def count (arr):
    counter = 0
    for _ in arr:
        counter += 1
    if counter <= 1:
        return 1
    return 1 + count(arr[1:])
# print(count(arr))

def max(arr):
    if len(arr) == 2:
        if arr[0] > arr[1]:
            return arr[0]
        else:
            return arr[1]
    maximum = max(arr[1:])
    if arr[0] > maximum:
        return arr[0]
    else:
        return maximum
# print(max(arr))

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    randomIndex = random.randrange(len(arr))
    pivot = arr[randomIndex]
    smaller = []
    bigger = []
    for i,num in enumerate(arr):
        if i == randomIndex:
            continue
        if (num <= pivot):
            smaller.append(num)
        else:
            bigger.append(num)
    return quick_sort(smaller) + [pivot] + quick_sort(bigger)

print(quick_sort([10,5,2,3]))
print(quick_sort([2,3,4,8,10]))
print(quick_sort(arr))

def get_multiplication_matrix(arr):
    result = []
    for i in range(1,11):
        result.append([j*i for j in arr])
    return result

multi_matrix = get_multiplication_matrix([2,3,4,8,10])
# for row in multi_matrix:
#     print(' '.join(map(str, row)))