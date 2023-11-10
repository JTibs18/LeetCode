# A company intends to give its employees a pay rise.
# Write a solution to modify the salary column by multiplying each salary by 2.

import pandas as pd 

# Attempt 1: uses less memory but more runtime 
def modifySalaryColumnV1(employees):
    employees['salary'] = employees['salary'].apply(lambda x: x * 2 )
    return employees

# Attempt 2: uses more memory but less runtime
def modifySalaryColumn(employees):
    employees['salary'] = employees['salary'] * 2
    return employees

# Test cases
data = [['Jack', 19666], 
        ['Piper', 74754], 
        ['Mia', 62509], 
        ['Ulysses', 54866]]
employees = pd.DataFrame(data, columns=['name', 'salary'])
print(modifySalaryColumn(employees))