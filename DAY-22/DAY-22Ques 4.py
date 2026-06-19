# Write a program to Remove spaces from string.

def remove_spaces(text):
    return text.replace(" ", "")

sentence = input("Enter a sentence: ")
print("String without spaces:", remove_spaces(sentence))
