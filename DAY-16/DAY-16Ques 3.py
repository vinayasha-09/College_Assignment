# Write a program to Find pair with given sum.

def find_pairs(arr, target_sum):
    pairs = []
    seen = set()
    
    for num in arr:
        complement = target_sum - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    
    return pairs


arr = [1, 4, 5, 3, 2, 7, 8]
target_sum = 9

result = find_pairs(arr, target_sum)
print("Pairs with sum", target_sum, "are:", result)
      
            # OR

#arr = [1, 4, 5, 3, 2, 7, 8]
#target_sum = 9

#for i in range(len(arr)):
#    for j in range(i+1, len(arr)):
#        if arr[i] + arr[j] == target_sum:
#            print("Pair:", arr[i], arr[j])
