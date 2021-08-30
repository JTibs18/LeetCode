# You are given an m x n matrix M initialized with all 0's and an array of operations ops, where ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.
# Count and return the number of maximum integers in the matrix after performing all the operations.

def maxCount(m, n, ops):
    if len(ops) == 0:
        return m * n
    else:
        minX = m
        minY = n
        for i in ops:
            if i[0] < minX:
                minX = i[0]
            if i[1] < minY:
                minY = i[1]
        return minX * minY

#Test cases
m = 3
n = 3
ops = [[2, 2], [3,3]]
print(maxCount(m, n, ops))

m = 3
n = 3
ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]
print(maxCount(m, n, ops))

m = 3
n = 3
ops = []
print(maxCount(m, n, ops))
