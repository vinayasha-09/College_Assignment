# Write a program to Check palindrome string.

def is_palindrome(s):
    # Convert to lowercase for case-insensitive check
    s = s.lower()
    # Compare string with its reverse
    return s == s[::-1]

text = input("Enter a string: ")
if is_palindrome(text):
    print(text, "is a palindrome")
else:
    print(text, "is not a palindrome")
