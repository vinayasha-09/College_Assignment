# Program to find diagonal sum of a matrix.

# Define a square matrix
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

# Initialize sum
diagonal_sum = 0

# Loop through matrix
for i in range(len(A)):
    diagonal_sum += A[i][i]   # main diagonal elements

# result
print("Matrix:")
for row in A:
    print(row)

print("\nSum of main diagonal elements =", diagonal_sum)
