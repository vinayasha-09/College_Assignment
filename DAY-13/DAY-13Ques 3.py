# Program to find largest and smallest element in an array

# Input array elements
arr = list(map(int, input("Enter elements separated by space: ").split()))

# Find largest and smallest
largest = max(arr)
smallest = min(arr)

# Display results
print("Array:", arr)
print("Largest element:", largest)
print("Smallest element:", smallest)
