# # Program to find intersection of two arrays

# Input arrays
arr1 = [1, 2, 3, 4]
arr2 = [3, 4, 5, 6]

# Intersection using set
intersection_array = list(set(arr1) & set(arr2))

# result
print("First array:", arr1)
print("Second array:", arr2)
print("Intersection of arrays:", intersection_array)
