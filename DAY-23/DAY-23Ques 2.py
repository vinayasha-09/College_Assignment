# Write a program to Find first repeating character.

def first_repeating(s):
    seen = set()   # to keep track of characters already seen
    
    for ch in s:
        if ch in seen:   # if character already appeared, it's repeating
            return ch
        seen.add(ch)
    return None   # if no repeating character found

text = input("Enter a string: ")
result = first_repeating(text)

if result:
    print("First repeating character is:", result)
else:
    print("No repeating character found.")
