# Write a program to Check symmetric matrix.

# Input: size of square matrix
n = int(input("Enter the size of the square matrix: "))

# Input matrix
print("Enter elements of the matrix:")
matrix = [[int(input()) for _ in range(n)] for _ in range(n)]

# Check symmetry
is_symmetric = True
for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            is_symmetric = False
            break

# Display result
if is_symmetric:
    print("The matrix is symmetric.")
else:
    print("The matrix is not symmetric.")
