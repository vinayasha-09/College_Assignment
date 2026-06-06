row = 5

for i in range(1, row + 1):
    for j in range(65,65+i):
        print(chr(64+i), end="")
    print()