# Write a program to Transpose matrix.

# Define a matrix
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

# Initialize result matrix with zeros
rows = len(A)
cols = len(A[0])
transpose = [[0 for _ in range(rows)] for _ in range(cols)]

# Perform transpose
for i in range(rows):
    for j in range(cols):
        transpose[j][i] = A[i][j]

# result
print("Original Matrix:")
for row in A:
    print(row)

print("\nTranspose Matrix:")
for row in transpose:
    print(row)
