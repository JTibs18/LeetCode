# Write a solution to calculate the bonus of each employee. The bonus of an employee is 100% of their salary if the ID of the employee is an odd number and the employee's name does not start with the character 'M'. The bonus of an employee is 0 otherwise.
# Return the result table ordered by employee_id.

import pandas as pd

def calculate_special_bonus(employees):
    bonus = []

    for i in employees.index: 
        if employees['employee_id'][i] % 2 != 0 and employees['name'][i][0] != "M":
            bonus.append(employees['salary'][i])
        else: 
            bonus.append(0)

    employees.insert(1, "bonus", bonus)
    return employees[['employee_id', 'bonus']].sort_values(by=['employee_id'])

# schema 
data = [[2, 'Meir', 3000], [3, 'Michael', 3800], [7, 'Addilyn', 7400], [8, 'Juan', 6100], [9, 'Kannon', 7700]]
Employees = pd.DataFrame(data, columns=['employee_id', 'name', 'salary']).astype({'employee_id':'int64', 'name':'object', 'salary':'int64'})
print(calculate_special_bonus(Employees))