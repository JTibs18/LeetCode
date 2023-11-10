# Write a solution to create a new column name bonus that contains the doubled values of the salary column.

import pandas as pd 

def createBonusColumn(employees): 
    employees['bonus'] = employees['salary'] * 2
    return employees

# Test cases 
data = [['Piper', 4548], 
        ['Grace', 28150], 
        ['Georgia', 1103], 
        ['Willow', 6593], 
        ['Finn', 74576],
        ['Thomas', 24433]]
employees = pd.DataFrame(data, columns=['name', 'salary'])
print(createBonusColumn(employees))