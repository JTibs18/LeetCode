# Write a solution to find all customers who never order anything.
# Return the result table in any order.

import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame): 
    df = customers.merge(orders, left_on="id", right_on='customerId', how="left")
    df = df[~df['customerId'].notnull()]
    df = df.rename(columns={'name' : 'Customers'})
    return df[['Customers']]

# schema 
data = [[1, 'Joe'], [2, 'Henry'], [3, 'Sam'], [4, 'Max']]
Customers = pd.DataFrame(data, columns=['id', 'name']).astype({'id':'Int64', 'name':'object'})
data = [[1, 3], [2, 1]]
Orders = pd.DataFrame(data, columns=['id', 'customerId']).astype({'id':'Int64', 'customerId':'Int64'})

print(find_customers(Customers, Orders))