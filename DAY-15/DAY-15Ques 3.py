# Write a program to Rotate array right.

def rotate_right(arr, d):
    n = len(arr)
    # slicing method
    return arr[-d:] + arr[:-d]

arr = [1, 2, 3, 4, 5]
d = 2   # number of positions to rotate
print("Original array:", arr)
print("Array after right rotation:", rotate_right(arr, d))
