# Write a program to Find common elements.

# Input arrays
arr1 = [1, 2, 3, 4, 7]
arr2 = [3, 4, 5, 6, 7]

common_elements = list(set(arr1) & set(arr2))

print("First array:", arr1)
print("Second array:", arr2)
print("Common elements:", common_elements)
