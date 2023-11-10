# There are some rows having missing values in the name column.
# Write a solution to remove the rows with missing values.

import pandas as pd 

# Attempt 1 
def dropMissingData1(students):
    return students.dropna(subset= ['name'])

# Attempt 2: faster runtime and less memory
def dropMissingData(students):
    return students[students['name'].notna()]

# Test cases
data = [[32, 'Piper', 5], 
        [217, None, 19],
        [779, 'Georgia', 20],
        [849, 'Willow', 14],
        [1, 'Jess', None]]
students = pd.DataFrame(data, columns=['student_id', 'name', 'age'])
print(dropMissingData(students))