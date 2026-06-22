# Write a program to Sort words by length.

words = ["apple", "banana", "kiwi", "grape", "watermelon"]

print("Original list of words:", words)

# Sort by length
words.sort(key=len)

print("Sorted by length:", words)
