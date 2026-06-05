#Write a program to Recursive Fibonacci.

def fib(n):
    if n <= 1:   # base case
        return n
    return fib(n - 1) + fib(n - 2)  # recursive call

# Input from user
num = int(input("Enter term number: "))
print("Fibonacci term at position", num, "is", fib(num))
