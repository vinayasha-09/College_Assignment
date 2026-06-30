# Program to find common characters in two strings

def common_characters(str1, str2):
    # Convert strings to sets to remove duplicates
    set1 = set(str1)
    set2 = set(str2)

    # Find intersection
    common = set1 & set2

    return ''.join(sorted(common))

s1 = "programming"
s2 = "gaming"

print("String 1:", s1)
print("String 2:", s2)
print("Common characters:", common_characters(s1, s2))
