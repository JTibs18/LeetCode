# There is an m x n matrix that is initialized to all 0's. There is also a 2D array indices where each indices[i] = [ri, ci] represents a 0-indexed location to perform some increment operations on the matrix.
# For each location indices[i], do both of the following:
# Increment all the cells on row ri.
# Increment all the cells on column ci.
# Given m, n, and indices, return the number of odd-valued cells in the matrix after applying the increment to all locations in indices.

def oddCells(m, n, indices): 
    oddCount = 0 
    finalMtrx = [[0 for x in range(n)] for y in range(m)]

    for r, c in indices: 
        for j in range(n): 
            finalMtrx[r][j] += 1 
        for k in range(m):
            finalMtrx[k][c] += 1 
    
    for indx, val in enumerate(finalMtrx): 
        for num in val: 
            if num % 2 != 0: 
                oddCount += 1

    return oddCount 

# Test cases
m = 2
n = 3
indices = [[0,1],[1,1]]
print(oddCells(m, n, indices))

m = 2
n = 2
indices = [[1,1],[0,0]]
print(oddCells(m, n, indices))
