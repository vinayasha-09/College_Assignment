# Centered Number Pyramid
rows = 5

for i in range(1, rows + 1):
    # Print spaces
    for j in range(rows - i):
        print(" ", end="")
    # Print increasing numbers
    for j in range(1, i + 1):
        print(j, end="")
    # Print decreasing numbers
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()
