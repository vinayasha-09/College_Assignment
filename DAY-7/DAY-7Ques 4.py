#Write a program to Recursive reverse number# Recursive reverse number program

def reverse_num(n, rev=0):
    if n == 0:   # base case
        return rev
    return reverse_num(n // 10, rev * 10 + (n % 10))  # recursive step

# Input from user
num = int(input("Enter a number: "))
print("Reversed number is:", reverse_num(num))
