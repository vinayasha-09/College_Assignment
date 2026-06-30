# Write a program to Linear search.

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i   # return index if found
    return -1          # return -1 if not found

numbers = [10, 25, 30, 45, 50]
search_item = int(input("Enter number to search: "))

result = linear_search(numbers, search_item)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
