# You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
# An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.
# Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
# The testcases are generated so that the answer will be less than or equal to 2 * 10^9.

def uniquePathsWithObstacles(obstacleGrid):
    if obstacleGrid[0][0] == 1:
        return 0

    def helper(m, n, memo = {}):
        curLocation = (m, n)

        if curLocation in memo:
            return memo[curLocation] 
        
        if m == len(obstacleGrid) - 1 and n == len(obstacleGrid[0]) - 1 and obstacleGrid[m][n] == 0:
            return 1
        
        memo[curLocation] = 0 

        if m + 1 < len(obstacleGrid) and obstacleGrid[m + 1][n] == 0:
            memo[curLocation] += helper(m + 1, n, memo)

        if n + 1 < len(obstacleGrid[m]) and obstacleGrid[m][n + 1] == 0: 
            memo[curLocation] += helper(m, n + 1, memo)
        
        return memo[curLocation]
    
    return helper(0, 0)

# Test cases
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
print(uniquePathsWithObstacles(obstacleGrid))

obstacleGrid = [[0,1],[0,0]]
print(uniquePathsWithObstacles(obstacleGrid))

obstacleGrid = [[0,0],[0,1]]
print(uniquePathsWithObstacles(obstacleGrid))

obstacleGrid = [[0]]
print(uniquePathsWithObstacles(obstacleGrid))

obstacleGrid = [[0], [0]]
print(uniquePathsWithObstacles(obstacleGrid))

obstacleGrid = [[0,0,0,0],[0,1,0,0],[0,0,0,0],[0,0,1,0],[0,0,0,0]]
print(uniquePathsWithObstacles(obstacleGrid))
