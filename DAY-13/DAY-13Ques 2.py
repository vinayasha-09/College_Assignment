# Program to find sum and average of an array

# Input array elements
arr = list(map(int, input("Enter elements separated by space: ").split()))

# Calculate sum
total = sum(arr)

# Calculate average
average = total / len(arr)

# Display results
print("Array:", arr)
print("Sum of array elements:", total)
print("Average of array elements:", average)
