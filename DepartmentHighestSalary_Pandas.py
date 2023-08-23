# Write a solution to find employees who have the highest salary in each of the departments.
# Return the result table in any order.

import pandas as pd 

def department_highest_salary(employee, department): 
    return employee.merge(department, left_on="departmentId", right_on='id', how='left', suffixes=('_employee', '_department')).groupby('departmentId').apply(lambda x: x[x['salary'] == x['salary'].max()]).reset_index(drop=True)[['name_department', 'name_employee', 'salary']].rename(columns={'name_department': 'Department', 'name_employee': 'Employee', 'salary': 'Salary'})

# schema
data = [[1, 'Joe', 70000, 1], [2, 'Jim', 90000, 1], [3, 'Henry', 80000, 2], [4, 'Sam', 60000, 2], [5, 'Max', 90000, 1]]
Employee = pd.DataFrame(data, columns=['id', 'name', 'salary', 'departmentId']).astype({'id':'Int64', 'name':'object', 'salary':'Int64', 'departmentId':'Int64'})
data = [[1, 'IT'], [2, 'Sales']]
Department = pd.DataFrame(data, columns=['id', 'name']).astype({'id':'Int64', 'name':'object'})
print(department_highest_salary(Employee, Department))