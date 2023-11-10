# Write a solution to calculate and display the number of rows and columns of players.
# Return the result as an array:
#   [number of rows, number of columns]

import pandas as pd 

def getDataframeSize(players): 
    rowSize = len(players.index)
    columnSize = len(players.columns)
    return [rowSize, columnSize]

# Test cases 
data = [[846, 'Mason', 21, 'Forward', 'RealMadrid'], 
        [749, 'Riley', 30, 'Winger', 'Barcelona'], 
        [155, 'Bob', 28, 'Striker', 'ManchesterUnited'], 
        [583, 'Isabella', 32, 'Goalkeeper', "Liverpool"],
        [388, 'Zachary', 24, 'Midfielder', 'BayernMunich'],
        [883, 'Ava', 23, "Defender", 'Chelsea'],
        [355, 'Violet', 18, 'Striker', 'Juventus'],
        [247, 'Thomas', 27, 'Striker', 'ParisSaint-Germain'],
        [761, "Jack", 27, "Midfielder", "ManchesterCity"], 
        [642, "Charlie", 36, "Center-back", "Arsenal"]]
players = pd.DataFrame(data, columns=['player_id', 'name', 'age', 'position', 'team'])
print(getDataframeSize(players))