# Write a solution to find the nth highest salary from the Employee table. If there is no nth highest salary, return null.

import pandas as pd 

def nth_highest_salary(employee, N): 
    return employee.sort_values(by='salary', ascending=False).drop_duplicates(subset='salary').iloc[N - 1:N][['salary']]

# schema 
data = [[1, 100], [2, 200], [3, 300]]
Employee = pd.DataFrame(data, columns=['id', 'salary']).astype({'id': 'int64', 'salary': 'int64'})
n = 2
print(nth_highest_salary(Employee, n))

data = [[1, 100]]
Employee = pd.DataFrame(data, columns=['id', 'salary']).astype({'id': 'int64', 'salary': 'int64'})
n = 2 
print(nth_highest_salary(Employee, n))

data = [[1, 100], [2, 100]]
Employee = pd.DataFrame(data, columns=['id', 'salary']).astype({'id': 'int64', 'salary': 'int64'})
n = 2 
print(nth_highest_salary(Employee, n))