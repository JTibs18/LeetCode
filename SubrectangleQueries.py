# Implement the class SubrectangleQueries which receives a rows x cols rectangle as a matrix of integers in the constructor and supports two methods:
# 1. updateSubrectangle(int row1, int col1, int row2, int col2, int newValue)
#   Updates all values with newValue in the subrectangle whose upper left coordinate is (row1,col1) and bottom right coordinate is (row2,col2).
# 2. getValue(int row, int col)
#   Returns the current value of the coordinate (row,col) from the rectangle.

class SubrectangleQueries:
    def __init__(self, rectangle):
        self.grid = rectangle

    def updateSubrectangle(self, row1, col1, row2, col2, newValue):
        for indxY in range(row1, row2 + 1):
            for indxX in range(col1, col2 + 1): 
                self.grid[indxY][indxX] = newValue 

    def getValue(self, row, col):
        return self.grid[row][col]

# Test case
subrectangleQueries = SubrectangleQueries([[1, 2, 1], [4, 3, 4], [3, 2, 1], [1, 1, 1]])
print(subrectangleQueries.getValue(0, 2))
subrectangleQueries.updateSubrectangle(0, 0, 3, 2, 5)
print(subrectangleQueries.getValue(0, 2))
print(subrectangleQueries.getValue(3, 1))
subrectangleQueries.updateSubrectangle(3, 0, 3, 2, 10)
print(subrectangleQueries.getValue(3, 1))
print(subrectangleQueries.getValue(0, 2))

subrectangleQueries = SubrectangleQueries([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
print(subrectangleQueries.getValue(0, 0))
subrectangleQueries.updateSubrectangle(0, 0, 2, 2, 100)
print(subrectangleQueries.getValue(0, 0))
print(subrectangleQueries.getValue(2, 2))
subrectangleQueries.updateSubrectangle(1, 1, 2, 2, 20)
print(subrectangleQueries.getValue(2, 2))
