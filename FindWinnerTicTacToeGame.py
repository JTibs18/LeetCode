# Tic-tac-toe is played by two players A and B on a 3 x 3 grid. The rules of Tic-Tac-Toe are:
# Players take turns placing characters into empty squares ' '.
# The first player A always places 'X' characters, while the second player B always places 'O' characters.
# 'X' and 'O' characters are always placed into empty squares, never on filled ones.
# The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
# The game also ends if all squares are non-empty.
# No more moves can be played if the game is over.
# Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that the ith move will be played on grid[rowi][coli]. return the winner of the game if it exists (A or B). In case the game ends in a draw return "Draw". If there are still movements to play return "Pending".
# You can assume that moves is valid (i.e., it follows the rules of Tic-Tac-Toe), the grid is initially empty, and A will play first.

def tictactoe(moves):
    playerMovesA = []
    playerMovesB = []

    def checkWin(playerMoves): 
        if [0, 0] in playerMoves and [0, 1] in playerMoves and [0, 2] in playerMoves:
            return True 
        if [1, 0] in playerMoves and [1, 1] in playerMoves and [1, 2] in playerMoves: 
            return True 
        if [2, 0] in playerMoves and [2, 1] in playerMoves and [2, 2] in playerMoves: 
            return True 
        if [0, 0] in playerMoves and [1, 0] in playerMoves and [2, 0] in playerMoves: 
            return True 
        if [0, 1] in playerMoves and [1, 1] in playerMoves and [2, 1] in playerMoves: 
            return True
        if [0, 2] in playerMoves and [1, 2] in playerMoves and [2, 2] in playerMoves: 
            return True
        if [0, 0] in playerMoves and [1, 1] in playerMoves and [2, 2] in playerMoves: 
            return True 
        if [0, 2] in playerMoves and [1, 1] in playerMoves and [2, 0] in playerMoves: 
            return True 
        
    for indx, val in enumerate(moves): 
        if indx % 2 == 0: 
            playerMovesA.append(val)
            if checkWin(playerMovesA) == True: 
                return "A"
        else: 
            playerMovesB.append(val)
            if checkWin(playerMovesB) == True:
                return "B"
            
    if len(moves) == 9:
        return "Draw"
    return "Pending"

# Test cases
moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
print(tictactoe(moves))

moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
print(tictactoe(moves))

moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
print(tictactoe(moves))
