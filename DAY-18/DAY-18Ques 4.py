# Write a program to Sort array in descending order

def sort_descending(arr):
    n = len(arr)
    # Bubble sort style (descending)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:   # swap if smaller
                arr[j], arr[j+1] = arr[j+1], arr[j]

numbers = [12, 4, 56, 23, 89, 1]
print("Original array:", numbers)

sort_descending(numbers)
print("Sorted in descending order:", numbers)
   
            # OR

#numbers = [12, 4, 56, 23, 89, 1]

#numbers.sort(reverse=True)   # built-in descending sort

#print("Sorted in descending order:", numbers)
