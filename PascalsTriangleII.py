# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above 

import math

# using pascal's triangle formula (slower runtime)
def getRow1(rowIndex):
    currentRow = [1 for _ in range(rowIndex + 1)]

    for i in range(1, rowIndex): 
        currentRow[i] = math.factorial(rowIndex) // (math.factorial(i) * math.factorial(rowIndex - i))

    return currentRow

# faster runtime 
def getRow(rowIndex):
    if rowIndex == 0: 
        return [1]
    
    curRow = [1 for _ in range(rowIndex + 1)]
    prevRow = getRow(rowIndex - 1)

    for i in range(1, rowIndex):
        curRow[i] = prevRow[i - 1] + prevRow[i]

    return curRow

# Test cases
rowIndex = 3
print(getRow(rowIndex))

rowIndex = 0
print(getRow(rowIndex))

rowIndex = 1 
print(getRow(rowIndex))