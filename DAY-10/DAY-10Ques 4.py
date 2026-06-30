# Centered Character Pyramid
rows = 5

for i in range(1, rows + 1):
    # Print spaces
    for j in range(rows - i):
        print(" ", end="")
    # Print increasing characters
    for j in range(65, 65 + i):   # ASCII 65 = 'A'
        print(chr(j), end="")
    # Print decreasing characters
    for j in range(65 + i - 2, 64, -1):
        print(chr(j), end="")
    print()
