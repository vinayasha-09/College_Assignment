# Write a program to Character frequency.

def char_frequency(text):
    freq = {}
    for ch in text:
        if ch != " ":   # ignore spaces
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
    return freq

sentence = input("Enter a sentence: ")
result = char_frequency(sentence)

print("Character frequencies:")
for char, count in result.items():
    print(char, ":", count)
