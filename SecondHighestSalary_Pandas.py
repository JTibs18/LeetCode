# Write a solution to find the second highest salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).

import pandas as pd

def second_highest_salary(employee): 
    df = employee['salary'].sort_values(ascending=False).drop_duplicates()
    if len(df) >= 2: 
        return pd.DataFrame({'secondHighestSalary':df.iloc[1:2]})
    return pd.DataFrame({'secondHighestSalary': [None]}) 

# schema 
data = [[1, 100], [2, 200], [3, 300]]
Employee = pd.DataFrame(data, columns=['id', 'salary']).astype({'id':'int64', 'salary':'int64'})
print(second_highest_salary(Employee))

data = [[1, 100]]
Employee = pd.DataFrame(data, columns=['id', 'salary']).astype({'id':'int64', 'salary':'int64'})
print(second_highest_salary(Employee))