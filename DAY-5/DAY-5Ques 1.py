#Write a program to Check perfect number.

num = int(input("Enter a number: "))
s = 0

for i in range(1, num):
    if num % i == 0:
        s += i

if s == num:
    print("Perfect Number")
else:
    print("Not Perfect Number")
