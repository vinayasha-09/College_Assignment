#Write a program to Recursive factorial.

def factorial(n):
    if n == 0 or n == 1:   # base case
        return 1
    else:
        return n * factorial(n - 1)  # recursive call

# Input from user
num = int(input("Enter a number: "))

print("Factorial of", num, "is", factorial(num))
