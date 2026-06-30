# Write a program to Compress a string.

def compress_string(s):
    compressed = ""
    count = 1
    
    # Loop through the string
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            compressed += s[i-1] + str(count)
            count = 1
    
    # Add the last character group
    compressed += s[-1] + str(count)
    
    return compressed

s = "aaabbccccd"
print("Original:", s)
print("Compressed:", compress_string(s))
