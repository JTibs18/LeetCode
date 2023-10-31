# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# 1. Each row must contain the digits 1-9 without repetition.
# 2. Each column must contain the digits 1-9 without repetition.
# 3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note: A Sudoku board (partially filled) could be valid but is not necessarily solvable.
#       Only the filled cells need to be validated according to the mentioned rules.

def isValidSudoku(board): 
    rowNumbers = dict()
    columnNumbers = dict()
    squareNumbers = dict()

    for indxRow, row in enumerate(board): 
        for indxCol, val in enumerate(row): 
            if val != '.': 
                squareRow = indxRow // 3
                squareCol = indxCol // 3 
                squareCoords = (squareRow, squareCol)

                if indxRow not in rowNumbers:
                    rowNumbers[indxRow] = [val]
                elif val in rowNumbers[indxRow]: 
                    return False 
                else: 
                    rowNumbers[indxRow].append(val)
                                    
                if indxCol not in columnNumbers: 
                    columnNumbers[indxCol] = [val]
                elif val in columnNumbers[indxCol]: 
                    return False
                else:
                    columnNumbers[indxCol].append(val)
                
                if squareCoords not in squareNumbers: 
                    squareNumbers[squareCoords] = [val]
                elif val in squareNumbers[(squareRow, squareCol)]: 
                    return False 
                else: 
                    squareNumbers[squareCoords].append(val)

    return True 

# Test cases
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(isValidSudoku(board))

board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(isValidSudoku(board))