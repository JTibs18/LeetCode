# Write a solution to concatenate these two DataFrames vertically into one DataFrame.

import pandas as pd 

def concatenateTables(df1, df2): 
    return pd.concat([df1, df2])

# Test cases
dataDF1 = [[1, 'Mason', 8], 
        [2, 'Ava', 6],
        [3, 'Taylor', 15],
        [4, 'Georgia', 17]]
dataDF2 = [[5, 'Leo', 7],
           [6, 'Alex', 7]]
df1 = pd.DataFrame(dataDF1, columns=['student_id', 'name', 'age'])
df2 = pd.DataFrame(dataDF2, columns=['student_id', 'name', 'age'])
print(concatenateTables(df1, df2))