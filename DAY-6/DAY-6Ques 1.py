# Convert decimal to binary..

num = int(input("Enter a decimal number: "))

binary = ""
while num > 0:
    remainder = num % 2
    binary = str(remainder) + binary
    num = num // 2

print("Binary number is:", binary)
