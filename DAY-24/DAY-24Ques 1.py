# Write a program to Check string rotation.

def is_rotation(s1, s2):
    # Check if lengths are equal
    if len(s1) != len(s2):
        return False
    
    # Concatenate s1 with itself
    temp = s1 + s1
    
    # If s2 is a substring of temp, it's a rotation
    return s2 in temp

s1 = "abcd"
s2 = "cdab"

if is_rotation(s1, s2):
    print("Yes, it's a rotation")
else:
    print("No, it's not a rotation")
