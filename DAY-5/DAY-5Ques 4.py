#Write a program to Find largest prime factor.

num = int(input("Enter a number: "))
i = 2
largest = 0

while num > 1:
    if num % i == 0:
        largest = i
        num //= i
    else:
        i += 1

print("Largest Prime Factor:", largest)
