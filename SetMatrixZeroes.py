# Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

def setZeroes(matrix):
    col = False
    count = 0

    #going through each value, setting outer most matrix indices to 0 when inner value is 0
    for i, val in enumerate(matrix):
        count += 1
        if 0 in val:
            for j, v in enumerate(val):
                if v == 0 and j == 0:
                    col = True
                elif v == 0 and i == 0:
                    matrix[0][0] = 0
                elif v == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

    #changing inner values if outer value is 0
    for i, val in enumerate(matrix[1:], start=1):
        for j, v in enumerate(val[1:], start=1):
            if matrix[i][0] == 0 or matrix [0][j] == 0:
                matrix[i][j] = 0
    #changing first row to 0 if indicator is 0
    if matrix[0][0] == 0:
        for i, val in enumerate(matrix):
            for j, val in enumerate(val):
                matrix[0][j] = 0
    #changing first column to 0 if indicator is 0
    if col == True:
        for i, val in enumerate(matrix):
            for j, val in enumerate(val):
                matrix[i][0] = 0

    print(matrix)

#Test cases
matrix = [[1,1,1],[1,0,1],[1,1,1]]
setZeroes(matrix)

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
setZeroes(matrix)

matrix = [[0,1]]
setZeroes(matrix)

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
setZeroes(matrix)
