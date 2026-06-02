# Program to find LCM of two numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

def lcm(x, y):
    return (x * y) // gcd(x, y)

print("LCM is", lcm(a, b))
      
          # OR

#import math

#a = int(input("Enter first number: "))
#b = int(input("Enter second number: "))

#print("LCM is", math.lcm(a, b))
