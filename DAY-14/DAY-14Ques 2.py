# Write a program to Frequency of an element.

def frequency(arr, target):
    count = 0
    for num in arr:
        if num == target:
            count += 1
    return count

numbers = [10, 20, 30, 20, 40, 20, 50]
x = int(input("Enter number to find frequency: "))

freq = frequency(numbers, x)
print(f"Frequency of {x} is {freq}")
    
              # OR

# numbers = [10, 20, 30, 20, 40, 20, 50]
# x = int(input("Enter number to find frequency: "))

# print("Frequency of", x, "is", numbers.count(x))
