# Given an m x n binary matrix mat, return the number of special positions in mat.
# A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).

# naive solution 
def numSpecial1(mat):
    onesCol = []
    onesRow = []
    ones = []
    count = 0

    for y, row in enumerate(mat):
        for x, val in enumerate(row): 
            if val == 1:
                onesCol.append(x)
                onesRow.append(y)
                ones.append((x, y))

    for x, y in ones: 
        if onesRow.count(y) == 1 and onesCol.count(x) == 1: 
            count += 1
    
    return count

# fastest solution, little less memory than first function
def numSpecial2(mat):
    onesCol = dict()
    onesRow = dict()
    ones = []
    count = 0

    for y, row in enumerate(mat):
        for x, val in enumerate(row): 
            if val == 1:
                if x not in onesCol:
                    onesCol[x] = 1
                else:
                    onesCol[x] += 1

                if y not in onesRow:
                    onesRow[y] = 1
                else: 
                    onesRow[y] += 1 

                ones.append((x, y))

    for x, y in ones: 
        if onesRow[y] == 1 and onesCol[x] == 1: 
            count += 1
    
    return count

# least memory usage, a little slower runtime than second function 
def numSpecial(mat):
    onesCol = dict()
    ones = []
    count = 0

    for y, row in enumerate(mat):
        for x, val in enumerate(row): 
            if val == 1:
                if x not in onesCol:
                    onesCol[x] = 1
                else:
                    onesCol[x] += 1

                if sum(row) == 1: 
                    ones.append((x, y))

    for x, y in ones: 
        if onesCol[x] == 1: 
            count += 1
    
    return count

# Test cases
mat = [[1,0,0],[0,0,1],[1,0,0]]
print(numSpecial(mat))

mat = [[1,0,0],[0,1,0],[0,0,1]]
print(numSpecial(mat))

mat = [[0,0,1,0],[0,0,0,0],[0,0,0,0],[0,1,0,0]]
print(numSpecial(mat))

mat = [[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,1],[0,0,0,0,1,0,0,0],[1,0,0,0,1,0,0,0],[0,0,1,1,0,0,0,0]]
print(numSpecial(mat))
