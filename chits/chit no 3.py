'''
Write a Python program to compute following computation on matrix:
a) Addition of two matrices	
b) Subtraction of two matrices
c) Multiplication of two matrices d) Transpose of a matrix

'''
def add_matrices(matrix1, matrix2):
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

def subtract_matrices(matrix1, matrix2):
    return [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

def multiply_matrices(matrix1, matrix2):
    return [[sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix2))) for j in range(len(matrix2[0]))] for i in range(len(matrix1))]

def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

# Example Matrices
matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Matrix a is:", matrix_a)
matrix_b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
print("Matrix b is:", matrix_b)

# a) Addition of two matrices
addition_result = add_matrices(matrix_a, matrix_b)

# b) Subtraction of two matrices
subtraction_result = subtract_matrices(matrix_a, matrix_b)

# c) Multiplication of two matrices
multiplication_result = multiply_matrices(matrix_a, matrix_b)

# d) Transpose of a matrix
transpose_result_a = transpose_matrix(matrix_a)
transpose_result_b = transpose_matrix(matrix_b)

# Display results
print("Addition Result:")
for row in addition_result:
    print(row)

print("Subtraction Result:")
for row in subtraction_result:
    print(row)

print("Multiplication Result:")
for row in multiplication_result:
    print(row)

print("Transpose of Matrix A:")
for row in transpose_result_a:
    print(row)

print("Transpose of Matrix B:")
for row in transpose_result_b:
    print(row)
