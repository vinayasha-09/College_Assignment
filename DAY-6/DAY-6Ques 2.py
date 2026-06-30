# Convert binary to decimal in a simple way

binary = input("Enter a binary number: ")

decimal = 0
power = 0

# Process digits from right to left
for digit in reversed(binary):
    decimal += int(digit) * (2 ** power)
    power += 1

print("Decimal number is:", decimal)
  
              #OR

# binary to decimal conversion

#binary = input("Enter a binary number: ")
#decimal = int(binary, 2)

#print("Decimal number is:", decimal)
