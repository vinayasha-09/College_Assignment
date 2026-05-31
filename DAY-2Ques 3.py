# write a program to find the product of digit in a no.

num = input("Enter a number: ")
product = 1
for digit in num:
    product *= int(digit)
print("Product of digits:", product)
