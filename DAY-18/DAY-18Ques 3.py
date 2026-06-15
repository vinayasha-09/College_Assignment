# Write a program to Binary search.

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2   # middle index

        if arr[mid] == target:
            return mid   # found
        elif arr[mid] < target:
            low = mid + 1   # search right half
        else:
            high = mid - 1  # search left half

    return -1   # not found


numbers = [10, 20, 30, 40, 50, 60, 70]
x = int(input("Enter number to search: "))

pos = binary_search(numbers, x)

if pos != -1:
    print("Found at index", pos)
else:
    print("Not found")
