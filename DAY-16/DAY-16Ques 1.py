# Write a program to Find missing number in array.

def find_missing(arr, n):
    # Formula for sum of first n natural numbers
    total = n * (n + 1) // 2
    # Subtract actual sum of array
    return total - sum(arr)

arr = [1, 2, 4, 5, 6]   # Missing number is 3
n = 6   # Numbers should be from 1 to 6

print("Missing number is:", find_missing(arr, n))
