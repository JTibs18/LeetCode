# Write a solution to rename the columns as follows:
#   id to student_id
#   first to first_name
#   last to last_name
#   age to age_in_years

import pandas as pd

def renameColumns(students):
    return students.rename(columns = {"id": "student_id", "first": "first_name", "last": "last_name", "age": "age_in_years"})

# Test cases
data = [[1, 'Mason', 'King', 6], [2, 'Ava', 'Wright', 7], [3, 'Taylor', 'Hall', 16], [4, 'Georgia', 'Thompson', 18], [5, 'Thomas', 'Moore', 10]]
students = pd.DataFrame(data, columns=['id', 'first', 'last', 'age'])
print(renameColumns(students))