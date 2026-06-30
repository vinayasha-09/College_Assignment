# Write a program to Find row-wise sum.

# Input: dimensions of matrix
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Input matrix
print("Enter elements of the matrix:")
matrix = [[int(input()) for _ in range(cols)] for _ in range(rows)]

# Calculate row-wise sum
print("Row-wise sums:")
for i in range(rows):
    row_sum = sum(matrix[i])
    print(f"Sum of row {i+1} = {row_sum}")
