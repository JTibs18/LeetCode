# Write a solution to report the product_name, year, and price for each sale_id in the Sales table.
# Return the resulting table in any order.

import pandas as pd

def sales_analysis(sales, product): 
    return sales.merge(product, on='product_id')[['product_name', 'year', 'price']]

# schema
data = [[1, 100, 2008, 10, 5000], [2, 100, 2009, 12, 5000], [7, 200, 2011, 15, 9000]]
Sales = pd.DataFrame(data, columns=['sale_id', 'product_id', 'year', 'quantity', 'price']).astype({'sale_id':'Int64', 'product_id':'Int64', 'year':'Int64', 'quantity':'Int64', 'price':'Int64'})
data = [[100, 'Nokia'], [200, 'Apple'], [300, 'Samsung']]
Product = pd.DataFrame(data, columns=['product_id', 'product_name']).astype({'product_id':'Int64', 'product_name':'object'})
print(sales_analysis(Sales, Product))