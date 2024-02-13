# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
# Note: You can only move either down or right at any point in time.

def minPathSum(grid):
    def helper(m, n, memo = {}):
        if (m, n) in memo:
            return memo[(m, n)]
        
        if m == len(grid) - 1 and n == len(grid[0]) - 1:
            return grid[m][n]
        
        memo[(m, n)] = grid[m][n]

        if m + 1 < len(grid) and n + 1 < len(grid[0]):
            memo[(m, n)] += min(helper(m + 1, n, memo), helper(m, n + 1, memo))
        elif m + 1 < len(grid):
            memo[(m, n)] += helper(m + 1, n, memo)
        elif n + 1 < len(grid[0]):
            memo[(m, n)] += helper(m, n + 1, memo)

        return memo[(m, n)]        
    
    return helper(0, 0)

# Test cases
grid = [[1,3,1],[1,5,1],[4,2,1]]
print(minPathSum(grid))

grid = [[1,2,3],[4,5,6]]
print(minPathSum(grid))
