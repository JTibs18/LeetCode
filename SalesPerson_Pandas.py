# Write a solution to find the names of all the salespersons who did not have any orders related to the company with the name "RED".
# Return the result table in any order.
# With help from https://leetcode.com/problems/sales-person/solutions/3970324/pandas-easy-to-understand-properly-commented/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd 

def sales_person(sales_person, company, orders):
    mergedTables = sales_person.merge(orders, on='sales_id', how='left').merge(company, on='com_id', how='left')
    filteredData = mergedTables[(mergedTables['name_y'] != 'RED') | (mergedTables['name_y'].isna())]
    result = filteredData[['name_x']].rename(columns={'name_x': 'name'}).drop_duplicates()
    salesWithRed = mergedTables[mergedTables['name_y'] == 'RED']['name_x'].unique()
    return result[~result['name'].isin(salesWithRed)]

# schema
data = [[1, 'John', 100000, 6, '4/1/2006'], [2, 'Amy', 12000, 5, '5/1/2010'], [3, 'Mark', 65000, 12, '12/25/2008'], [4, 'Pam', 25000, 25, '1/1/2005'], [5, 'Alex', 5000, 10, '2/3/2007']]
SalesPerson = pd.DataFrame(data, columns=['sales_id', 'name', 'salary', 'commission_rate', 'hire_date']).astype({'sales_id':'Int64', 'name':'object', 'salary':'Int64', 'commission_rate':'Int64', 'hire_date':'datetime64[ns]'})
data = [[1, 'RED', 'Boston'], [2, 'ORANGE', 'New York'], [3, 'YELLOW', 'Boston'], [4, 'GREEN', 'Austin']]
Company = pd.DataFrame(data, columns=['com_id', 'name', 'city']).astype({'com_id':'Int64', 'name':'object', 'city':'object'})
data = [[1, '1/1/2014', 3, 4, 10000], [2, '2/1/2014', 4, 5, 5000], [3, '3/1/2014', 1, 1, 50000], [4, '4/1/2014', 1, 4, 25000]]
Orders = pd.DataFrame(data, columns=['order_id', 'order_date', 'com_id', 'sales_id', 'amount']).astype({'order_id':'Int64', 'order_date':'datetime64[ns]', 'com_id':'Int64', 'sales_id':'Int64', 'amount':'Int64'})
print(sales_person(SalesPerson, Company, Orders))