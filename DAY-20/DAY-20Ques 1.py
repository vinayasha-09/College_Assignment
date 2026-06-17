# Write a program to Multiply matrices.

# Input: dimensions of matrices
rows_A = int(input("Enter number of rows in Matrix A: "))
cols_A = int(input("Enter number of columns in Matrix A: "))
rows_B = int(input("Enter number of rows in Matrix B: "))
cols_B = int(input("Enter number of columns in Matrix B: "))

# Check if multiplication is possible
if cols_A != rows_B:
    print("Matrix multiplication not possible!")
else:
    # Input Matrix A
    print("Enter elements of Matrix A:")
    A = [[int(input()) for _ in range(cols_A)] for _ in range(rows_A)]

    # Input Matrix B
    print("Enter elements of Matrix B:")
    B = [[int(input()) for _ in range(cols_B)] for _ in range(rows_B)]

    # Resultant Matrix C
    C = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    # Matrix multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]

    # result
    print("Resultant Matrix after multiplication:")
    for row in C:
        print(row)
