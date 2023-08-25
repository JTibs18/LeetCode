# Write a solution to rearrange the Products table so that each row has (product_id, store, price). If a product is not available in a store, do not include a row with that product_id and store combination in the result table.
# Return the result table in any order.
# With help from https://leetcode.com/problems/rearrange-products-table/solutions/3934345/pandas-simple-easy-solution-beginner-friendly/
# With help from https://leetcode.com/problems/rearrange-products-table/solutions/3890418/pandas-a-very-short-and-simple-solution/

import pandas as pd 

def rearrange_products_table1(products): 
    result_rows = []

    for _, row in products.iterrows():
        for store in ['store1', 'store2', 'store3']:
            price = row[store]

            if pd.notna(price):
                result_rows.append((row['product_id'], store, price))
    
    return pd.DataFrame(result_rows, columns=['product_id', 'store', 'price']).astype({'product_id': 'int64', 'store': 'object', 'price':"int64"})

def rearrange_products_table(products): 
    return products.melt(
        id_vars = ['product_id'],
        value_vars = ['store1', 'store2', 'store3'],
        var_name = 'store',
        value_name = 'price'
    ).dropna()

# schema 
data = [[0, 95, 100, 105], [1, 70, None, 80]]
Products = pd.DataFrame(data, columns=['product_id', 'store1', 'store2', 'store3'])
print(rearrange_products_table(Products))