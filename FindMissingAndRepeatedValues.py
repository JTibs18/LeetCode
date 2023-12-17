# You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, n2]. Each integer appears exactly once except a which appears twice and b which is missing. The task is to find the repeating and missing numbers a and b.
# Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b.
# Question 1 for Weekly Contest 376

def findMissingAndRepeatedValues(grid):
    returnArray = [0, 0]
    valAppearances = dict()

    for i in grid:
        for j in i:
            if j in valAppearances:
                valAppearances[j] += 1
            else: 
                valAppearances[j] = 1

    for i in range(1, len(grid) * len(grid[0]) + 1):
        if i in valAppearances and valAppearances[i] != 1:
            returnArray[0] = i 
        elif i not in valAppearances:
            returnArray[1] = i

    return returnArray

# Test cases
grid = [[1, 3], [2, 2]]
print(findMissingAndRepeatedValues(grid))

grid = [[9, 1, 7], [8, 9, 2], [3, 4, 6]]
print(findMissingAndRepeatedValues(grid))
