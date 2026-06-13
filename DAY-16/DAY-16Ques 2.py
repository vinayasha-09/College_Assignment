# Write a program to Find maximum frequency element.

def max_frequency_element(arr):
    freq = {}
    
    # Count frequency of each element
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    
    # Find element with maximum frequency
    max_elem = max(freq, key=freq.get)
    return max_elem, freq[max_elem]

arr = [1, 2, 2, 3, 1, 2, 4, 1, 1]
element, frequency = max_frequency_element(arr)
print("Element with maximum frequency:", element)
print("Frequency:", frequency)

             # OR
             
#from collections import Counter

#arr = [1, 2, 2, 3, 1, 2, 4, 1, 1]
#counter = Counter(arr)

#element, frequency = counter.most_common(1)[0]
#print("Element with maximum frequency:", element)
#print("Frequency:", frequency)
