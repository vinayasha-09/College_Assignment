#Write a program to Find maximum occurring character.

def max_occurring_char(s):
    freq = {}   # dictionary to store frequency of each character
    
    # Count frequency of each character
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    
    # Find character with maximum frequency
    max_char = max(freq, key=freq.get)
    return max_char, freq[max_char]

text = input("Enter a string: ")
char, count = max_occurring_char(text)
print("Maximum occurring character is:", char)
print("It occurs", count, "times.")
