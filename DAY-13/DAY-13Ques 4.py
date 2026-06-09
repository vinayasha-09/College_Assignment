# Program to count even and odd elements in an array

# Input array elements
arr = list(map(int, input("Enter elements separated by space: ").split()))

# Initialize counters
even_count = 0
odd_count = 0

# Count even and odd
for num in arr:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# Display results
print("Array:", arr)
print("Number of even elements:", even_count)
print("Number of odd elements:", odd_count)
