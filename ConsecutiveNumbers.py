# Find all numbers that appear at least three times consecutively.
# Return the result table in any order.

import pandas as pd

def consecutive_numbers(logs):
    twoConsecutiveRows = (logs.num.diff() == 0)
    threeConsecutiveRows = (logs.num.diff().diff() == 0)
    return logs[twoConsecutiveRows & threeConsecutiveRows][['num']].drop_duplicates().rename(columns={'num':'ConsecutiveNums'})

# Test cases
data = [[1, 1],
        [2, 1],
        [3, 1],
        [4, 2],
        [5, 1],
        [6, 2],
        [7, 2]]
logs = pd.DataFrame(data, columns=['id', 'num'])
print(consecutive_numbers(logs))