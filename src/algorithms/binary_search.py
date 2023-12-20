def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low < high:
        mid = round((high - low) / 2)
        guess = list[mid]
        print(mid, guess)
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        elif guess < item:
            low = mid + 1
    return None
    
my_list = [1,3,5,7,9]
print(binary_search(my_list, 3), 1)
print(binary_search(my_list, -1), 'None')