# Write a solution to find for each date the number of different products sold and their names.
# The sold products names for each date should be sorted lexicographically.
# Return the result table ordered by sell_date.

import pandas as pd 

def categorize_products(activities): 
    return activities.groupby('sell_date')['product'].agg([('num_sold', 'nunique'), ('products', lambda x: ','.join(sorted(x.unique())))]).reset_index()

# schema
data = [['2020-05-30', 'Headphone'], ['2020-06-01', 'Pencil'], ['2020-06-02', 'Mask'], ['2020-05-30', 'Basketball'], ['2020-06-01', 'Bible'], ['2020-06-02', 'Mask'], ['2020-05-30', 'T-Shirt']]
Activities = pd.DataFrame(data, columns=['sell_date', 'product']).astype({'sell_date':'datetime64[ns]', 'product':'object'})
print(categorize_products(Activities))