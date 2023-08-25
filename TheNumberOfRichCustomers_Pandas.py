# Write a solution to report the number of customers who had at least one bill with an amount strictly greater than 500.
# With help from https://leetcode.com/problems/the-number-of-rich-customers/solutions/3946130/pandas-2-line-solution-for-beginners/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd

def count_rich_customers1(store): 
    df = store.groupby(by='customer_id')[['amount']].max()
    return pd.DataFrame({"rich_count": [len(df[df['amount'] > 500])]}) 

def count_rich_customers(store):
    richCustomersCount = store[store['amount'] > 500]['customer_id'].nunique()
    return pd.DataFrame([richCustomersCount], columns=['rich_count'])

# schema 
data = [[6, 1, 549], [8, 1, 834], [4, 2, 394], [11, 3, 657], [13, 3, 257]]
Store = pd.DataFrame(data, columns=['bill_id', 'customer_id', 'amount']).astype({'bill_id':'int64', 'customer_id':'int64', 'amount':'int64'})
print(count_rich_customers(Store))