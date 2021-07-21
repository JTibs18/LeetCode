# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

def countNegatives(grid):
    count = 0
    for val in grid:
        for num in val:
            if num < 0:
                count += 1

    return count

#Test cases
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(countNegatives(grid))

grid = [[3,2],[1,0]]
print(countNegatives(grid))

grid = [[1,-1],[-1,-1]]
print(countNegatives(grid))

grid = [[-1]]
print(countNegatives(grid))
