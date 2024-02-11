# Given a 0-indexed m x n integer matrix matrix, create a new 0-indexed matrix called answer. Make answer equal to matrix, then replace each element with the value -1 with the maximum element in its respective column.
# Return the matrix answer.
# For Weekly Contest #384 Question 1

def modifiedMatrix(matrix):
    maxCols = dict()

    for row in matrix:
        for indxCol, col in enumerate(row):
            if indxCol not in maxCols:
                maxCols[indxCol] = col 
            else:
                maxCols[indxCol] = max(maxCols[indxCol], col)
        
    for indxRow, row in enumerate(matrix):
        for indxCol, col in enumerate(row):
            if col == -1:
                matrix[indxRow][indxCol] = maxCols[indxCol]

    return matrix

# Test cases
matrix = [[1,2,-1],[4,-1,6],[7,8,9]]
print(modifiedMatrix(matrix))

matrix = [[3,-1],[5,2]]
print(modifiedMatrix(matrix))
