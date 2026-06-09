# Program to input and display an array

# Input size of array
n = int(input("Enter number of elements: "))

# Initialize empty list
arr = []

# Input elements
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)

# Display array
print("The array is:", arr)
