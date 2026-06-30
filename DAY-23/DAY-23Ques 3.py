# Write a program to Check anagram strings.

def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase for fair comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Sort both strings and compare
    return sorted(str1) == sorted(str2)

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if are_anagrams(s1, s2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
