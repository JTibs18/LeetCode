# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.

def searchMatrix(matrix, target):
    for row in matrix:
        if row[0] <= target and row[len(row) - 1] >= target:
            for element in row:
                if element == target:
                    return True
            return False
    return False

#Test Cases
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(searchMatrix(matrix, target))

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13
print(searchMatrix(matrix, target))
