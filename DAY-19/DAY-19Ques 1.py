# Write a program to Add matrices.

def add_matrices(A, B):
    rows = len(A)
    cols = len(A[0])
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            result[i][j] = A[i][j] + B[i][j]
    return result
 
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

print("Matrix A:")
for row in A:
    print(row)

print("\nMatrix B:")
for row in B:
    print(row)

sum_matrix = add_matrices(A, B)

print("\nSum of matrices:")
for row in sum_matrix:
    print(row)
