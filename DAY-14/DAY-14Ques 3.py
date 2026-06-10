# Write a program to Second largest element.

def second_largest(arr):
    arr = list(set(arr))   # remove duplicates.
    arr.sort()             # sort the list in assending order.
    if len(arr) < 2:
        return None        # no second largest if less than 2 elements
    return arr[-2]         # second last element is second largest

numbers = [10, 20, 4, 45, 99, 99, 67]
print("Second largest element is:", second_largest(numbers))
      