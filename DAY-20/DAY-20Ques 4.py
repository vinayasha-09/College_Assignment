# Write a program to Find column-wise sum.

# Input: dimensions of matrix
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Input matrix
print("Enter elements of the matrix:")
matrix = [[int(input()) for _ in range(cols)] for _ in range(rows)]

# Calculate column-wise sum.
print("Column-wise sums:")
for j in range(cols):
    col_sum = 0
    for i in range(rows):
        col_sum += matrix[i][j]
    print(f"Sum of column {j+1} = {col_sum}")
