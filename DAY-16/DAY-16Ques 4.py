# Write a program to Remove duplicates from array.

def remove_duplicates(arr):
    # Convert list to set (removes duplicates), then back to list
    return list(set(arr))

arr = [1, 2, 2, 3, 4, 4, 5, 1, 6]
print("Array without duplicates:", remove_duplicates(arr))
