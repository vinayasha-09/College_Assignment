# Write a program to Find first non-repeating character.

def first_non_repeating(s):
    for i in range(len(s)):
        if s.count(s[i]) == 1:   # check if character occurs only once
            return s[i]
    return None   # if no non-repeating character found

text = input("Enter a string: ")
result = first_non_repeating(text)

if result:
    print("First non-repeating character is:", result)
else:
    print("No non-repeating character found.")
