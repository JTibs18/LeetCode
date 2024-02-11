# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
# The test cases are generated so that the answer will be less than or equal to 2 * 109.
# with help from https://www.youtube.com/watch?v=oBt53YbR9Kk&t=857s

def uniquePaths(m, n):
    def helper(m, n, memo = {}):
        curLocation = tuple(sorted((m, n)))
        
        if curLocation in memo:
            return memo[curLocation] 
        
        if m == 1 and n == 1:
            return 1
        
        if m == 0 or n == 0:
            return 0 
        
        memo[curLocation] = helper(m - 1, n, memo) + helper(m, n - 1, memo)
        return memo[curLocation]
    
    return helper(m, n)

# Test cases
m = 3
n = 7
print(uniquePaths(m, n))

m = 3
n = 2 
print(uniquePaths(m, n))
