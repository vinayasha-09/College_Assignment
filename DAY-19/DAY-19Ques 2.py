# Write a program to Subtract matrices.

# Define two matrices
A = [[5, 7, 9],
     [4, 6, 8],
     [3, 2, 1]]

B = [[1, 2, 3],
     [3, 2, 1],
     [4, 5, 6]]

# Initialize result matrix with zeros
result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

# Perform subtraction
for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j] = A[i][j] - B[i][j]

# result
print("Matrix A:")
for row in A:
    print(row)

print("\nMatrix B:")
for row in B:
    print(row)

print("\nResult of A - B:")
for row in result:
    print(row)
