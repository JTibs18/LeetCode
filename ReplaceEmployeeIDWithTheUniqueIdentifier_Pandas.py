# Write a solution to show the unique ID of each user, If a user does not have a unique ID replace just show null.
# Return the result table in any order.

import pandas as pd

def replace_employee_id(employees, employee_uni):
    return employees.merge(employee_uni, left_on='id', right_on='id', how='left')[['unique_id', 'name']]

# schema
data = [[1, 'Alice'], [7, 'Bob'], [11, 'Meir'], [90, 'Winston'], [3, 'Jonathan']]
Employees = pd.DataFrame(data, columns=['id', 'name']).astype({'id':'int64', 'name':'object'})
data = [[3, 1], [11, 2], [90, 3]]
EmployeeUNI = pd.DataFrame(data, columns=['id', 'unique_id']).astype({'id':'int64', 'unique_id':'int64'})
print(replace_employee_id(Employees, EmployeeUNI))