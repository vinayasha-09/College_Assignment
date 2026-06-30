#Write a program to Recursive sum of digits.

def sum_digits(n):
    if n == 0:   # base case
        return 0
    return (n % 10) + sum_digits(n // 10)  # recursive call

# Input from user
num = int(input("Enter a number: "))
print("Sum of digits =", sum_digits(num))
