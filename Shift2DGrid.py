# Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.
# In one shift operation:
# Element at grid[i][j] moves to grid[i][j + 1].
# Element at grid[i][n - 1] moves to grid[i + 1][0].
# Element at grid[m - 1][n - 1] moves to grid[0][0].
# Return the 2D grid after applying shift operation k times.

# References: 
#             https://www.geeksforgeeks.org/python-ways-to-flatten-a-2d-list/ 
#             https://www.geeksforgeeks.org/python-remove-last-k-elements-of-list/ 
#             https://stackoverflow.com/questions/17483557/python-transforming-one-dimensional-array-into-two-dimensional-array 

def shiftGrid(grid, k): 
    rowLength = len(grid[0])
    totalElements = rowLength * len(grid)

    if totalElements < k: 
        k = k % totalElements

    if k == 0: 
        return grid 

    flattenGrid = [i for num in grid for i in num]
    shift = flattenGrid[-k::]
    endSection = flattenGrid[:len(flattenGrid) - k]
    shift.extend(endSection)
    
    return [shift[i:i + rowLength] for i in range(0, len(shift), rowLength)]

# Test cases
grid = [[1,2,3],[4,5,6],[7,8,9]] 
k = 1
print(shiftGrid(grid, k))

grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
k = 4
print(shiftGrid(grid, k))

grid = [[1,2,3],[4,5,6],[7,8,9]]
k = 9
print(shiftGrid(grid, k))

grid = [[1],[2],[3],[4],[7],[6],[5]]
k = 23
print(shiftGrid(grid, k))
