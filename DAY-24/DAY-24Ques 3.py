# Write a program to Find longest word.

def find_longest_word(sentence):
    words = sentence.split()   # split sentence into words
    longest = ""
    
    for word in words:
        if len(word) > len(longest):
            longest = word
    
    return longest

sentence = "I love programming in Python"
print("Sentence:", sentence)
print("Longest word:", find_longest_word(sentence))
