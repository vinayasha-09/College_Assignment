# Write a program to Remove duplicate characters.

def remove_duplicates(s):
    result = ""
    seen = set()
    
    for ch in s:
        if ch not in seen:
            result += ch
            seen.add(ch)
    
    return result

s = "programming"
print("Original:", s)
print("Without duplicates:", remove_duplicates(s))
