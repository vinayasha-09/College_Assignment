# Write a program to Selection sort.

def selection_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n-1):
        # Find the minimum element in remaining unsorted array
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

numbers = [64, 25, 12, 22, 11]
print("Original array:", numbers)

selection_sort(numbers)
print("Sorted array:", numbers)
