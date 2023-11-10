# Write a solution to correct the errors:
# The grade column is stored as floats, convert it to integers.

import pandas as pd 

def changeDatatype(students):
    return students.astype({'grade': 'int'})

# Test cases
data = [[1, 'Ava', 6, 73.0],
        [2, 'Kate', 15, 87.0]]
students = pd.DataFrame(data, columns=['student_id', 'name', 'age', 'grade'])
print(changeDatatype(students))