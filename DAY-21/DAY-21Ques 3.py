# Write a program to Count vowels and consonants.

string = input("Enter a string: ")
string = string.lower()   # convert to lowercase for easy checking

vowels = "aeiou"
vowel_count = 0
consonant_count = 0

for char in string:
    if char.isalpha():   # check only letters
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Vowels =", vowel_count)
print("Consonants =", consonant_count)
