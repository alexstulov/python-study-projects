arr = [1,2,3,7,4,5,6]
def sum (arr):
    if len(arr) == 1:
        return arr[0]
    return arr[0] + sum(arr[1:])

print(sum(arr))

def count (arr):
    counter = 0
    for _ in arr:
        counter += 1
    if counter <= 1:
        return 1
    return 1 + count(arr[1:])

print(count(arr))

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

print(max(arr))