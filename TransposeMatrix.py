# Given a 2D integer array matrix, return the transpose of matrix.
# The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

def transpose(matrix):
    newMatrix = [[0] * len(matrix) for _ in range(len(matrix[0]))]

    for y, row in enumerate(matrix):
        for x, val in enumerate(row): 
            newMatrix[x][y] = val

    return newMatrix 

# Test cases
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(transpose(matrix))

matrix = [[1,2,3],[4,5,6]]
print(transpose(matrix))
