# Write a program to Count words in a sentence.

def count_words(sentence):
    # Split sentence into words using spaces
    words = sentence.split()
    return len(words)

text = input("Enter a sentence: ")
print("Number of words:", count_words(text))
