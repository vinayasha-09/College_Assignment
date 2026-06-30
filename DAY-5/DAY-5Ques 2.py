#Write a program to Check strong number.

num = int(input("Enter a number: "))
temp = num
s = 0

while temp > 0:
    digit = temp % 10
    fact = 1
    for i in range(1, digit + 1):
        fact *= i
    s += fact
    temp //= 10

if s == num:
    print("Strong Number")
else:
    print("Not Strong Number")
