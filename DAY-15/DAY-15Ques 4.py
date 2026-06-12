# Write a program to Move zeroes to end.

def move_zeroes(arr):
    result = []
    count = 0
    
    # collect non-zero elements
    for num in arr:
        if num != 0:
            result.append(num)
        else:
            count += 1
    
    # add zeroes at the end
    result.extend([0] * count)
    return result

arr = [0, 1, 9, 0, 3, 0, 5, 0]
print("Original array:", arr)
print("Array after moving zeroes:", move_zeroes(arr))
