# Write a program to Find duplicates in array.

def find_duplicates(arr):
    duplicates = []
    for i in arr:
        if arr.count(i) > 1 and i not in duplicates:
            duplicates.append(i)
    return duplicates

numbers = [10, 20, 30, 20, 40, 50, 10, 30]
print("Duplicates are:", find_duplicates(numbers))
