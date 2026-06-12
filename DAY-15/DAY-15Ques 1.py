# Write a program to Reverse array.

def reverse_array(arr):
    n = len(arr)
    rev = []
    for i in range(n-1, -1, -1):   # start from last index to 0
        rev.append(arr[i])
    return rev

arr = [1, 2, 3, 4, 5]
print("Original array:", arr)
print("Reversed array:", reverse_array(arr))
          
            # OR

#arr = [1, 2, 3, 4, 5]

# reverse using slicing
#rev = arr[::-1]

#print("Original array:", arr)
#print("Reversed array:", rev)
