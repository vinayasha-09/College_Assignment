# Write a program to Find string length without strlen().

string = input("Enter a string: ")
count = 0

for char in string:   # loop through each character
    count += 1

print("Length of string =", count)

