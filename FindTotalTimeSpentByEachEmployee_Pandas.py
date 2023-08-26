# Write a solution to calculate the total time in minutes spent by each employee on each day at the office. Note that within one day, an employee can enter and leave more than once. The time spent in the office for a single entry is out_time - in_time.
# Return the result table in any order.

import pandas as pd

def total_time(employees): 
    employees['total_time'] = employees['out_time'] - employees['in_time']
    employees = employees.groupby(by=['event_day', 'emp_id'])['total_time'].sum().reset_index()
    return employees.rename(columns={'event_day': 'day'})

# schema 
data = [['1', '2020-11-28', '4', '32'], ['1', '2020-11-28', '55', '200'], ['1', '2020-12-3', '1', '42'], ['2', '2020-11-28', '3', '33'], ['2', '2020-12-9', '47', '74']]
Employees = pd.DataFrame(data, columns=['emp_id', 'event_day', 'in_time', 'out_time']).astype({'emp_id':'Int64', 'event_day':'datetime64[ns]', 'in_time':'Int64', 'out_time':'Int64'})
print(total_time(Employees))