# Write a program to Print multiplication table of a given number.

num = int(input("Enter a number: "))

print(f"Multiplication Table of {num}")
for i in range(1, 11):   # printing table up to 10
    print(f"{num} x {i} = {num * i}")
