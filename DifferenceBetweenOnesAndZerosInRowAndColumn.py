# You are given a 0-indexed m x n binary matrix grid.
# A 0-indexed m x n difference matrix diff is created with the following procedure:
#   Let the number of ones in the ith row be onesRowi.
#   Let the number of ones in the jth column be onesColj.
#   Let the number of zeros in the ith row be zerosRowi.
#   Let the number of zeros in the jth column be zerosColj.
#   diff[i][j] = onesRowi + onesColj - zerosRowi - zerosColj
# Return the difference matrix diff.

def onesMinusZeros(grid):
    transposedGrid = [[grid[j][i] for j in range(len(grid))] for i in range (len(grid[0]))]
    transposedGridCount = dict()
    newGrid = []

    for i in range(len(transposedGrid)):
        transposedGridCount[i] = transposedGrid[i].count(1)

    for row in grid: 
        onesRow = row.count(1)
        zerosRow = row.count(0)
        curRow = []

        for indx in range(len(row)): 
            onesCol = transposedGridCount[indx] 
            zerosCol = len(transposedGrid[indx]) - onesCol
            curRow.append(onesRow + onesCol - zerosRow - zerosCol)
        
        newGrid.append(curRow)
    
    return newGrid

# Test cases
grid = [[0,1,1],[1,0,1],[0,0,1]]
print(onesMinusZeros(grid))

grid = [[1,1,1],[1,1,1]]
print(onesMinusZeros(grid))
