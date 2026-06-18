# Write a program to Convert lowercase to uppercase.

string = input("Enter a string: ")
result = ""

for char in string:
    # check if character is lowercase (a-z)
    if 'a' <= char <= 'z':
        # convert to uppercase by subtracting 32 from ASCII value
        result += chr(ord(char) - 32)
    else:
        result += char   # keep other characters unchanged

print("Uppercase string =", result)
