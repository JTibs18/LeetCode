# Given a square matrix mat, return the sum of the matrix diagonals.
# Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

def diagonalSum(mat):
    p1 = 0
    p2 = len(mat[0]) - 1
    s = 0

    for val in mat:
        if p1 == p2:
            s += val[p1]
        else:
            s += val[p1]
            s += val[p2]

        p1 += 1
        p2 -= 1
        
    return s

#Test cases
mat = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
print(diagonalSum(mat))

mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
print(diagonalSum(mat))

mat = [[5]]
print(diagonalSum(mat))
