# Write a solution to find managers with at least five direct reports.
# Return the result table in any order.

import pandas as pd

def find_managers(employee): 
    managerCount = employee.groupby('managerId').agg(direct_report_count=('id', 'count')).reset_index()
    managerCount = managerCount[managerCount['direct_report_count'] >= 5]
    return employee.merge(managerCount, left_on='id', right_on='managerId')[['name']]

# schema
data = [[101, 'John', 'A', None], [102, 'Dan', 'A', 101], [103, 'James', 'A', 101], [104, 'Amy', 'A', 101], [105, 'Anne', 'A', 101], [106, 'Ron', 'B', 101], [107, 'Tony', 'C', 102]]
Employee = pd.DataFrame(data, columns=['id', 'name', 'department', 'managerId']).astype({'id':'Int64', 'name':'object', 'department':'object', 'managerId':'Int64'})
print(find_managers(Employee))