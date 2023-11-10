# Write a solution to select the name and age of the student with student_id = 101.

import pandas as pd

def selectData(students):
    return students[students['student_id'] == 101][["name", "age"]]

# Test cases
data = [[101, "Ulysses", 13],
        [53, 'William', 10],
        [128, "Henry", 6], 
        [3, "Henry", 11]]
students = pd.DataFrame(data, columns=["student_id", "name", "age"])
print(selectData(students))