# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it

def generate(numRows): 
    if numRows == 0:
        return []
    
    if numRows == 1: 
        return [[1]]
    
    curRow = [1 for _ in range(numRows)]
    previousRow = generate(numRows - 1)

    for i in range(1, numRows - 1):
        curRow[i] = previousRow[numRows - 2][i - 1] + previousRow[numRows - 2][i]
    
    previousRow.append(curRow)
    return previousRow

# Test cases
numRows = 5
print(generate(numRows))

numRows = 1
print(generate(numRows))