# Count set bits in a number

num = int(input("Enter a number: "))

count = 0
while num > 0:
    if num % 2 == 1:   # check if last bit is 1
        count += 1
    num = num // 2     # shift right

print("Number of set bits:", count)
