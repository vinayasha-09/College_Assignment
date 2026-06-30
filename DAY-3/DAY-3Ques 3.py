# Program to find GCD of two numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while b != 0:
    a, b = b, a % b   # Euclidean algorithm

print("GCD is", a)
    
     # OR

#import math

#a = int(input("Enter first number: "))
#b = int(input("Enter second number: "))

#print("GCD is", math.gcd(a, b))