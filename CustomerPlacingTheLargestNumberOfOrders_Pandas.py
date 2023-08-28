# Write a solution to find the customer_number for the customer who has placed the largest number of orders.
# The test cases are generated so that exactly one customer will have placed more orders than any other customer.
# Follow up: What if more than one customer has the largest number of orders, can you find all the customer_number in this case?

import pandas as pd

def largest_orders(orders): 
    orders = orders.groupby('customer_number')['order_number'].count().reset_index()
    return orders[orders['order_number'] == orders['order_number'].max()][['customer_number']]

# schema
data = [[1, 1], [2, 2], [3, 3], [4, 3], [5, 2]]
Orders = pd.DataFrame(data, columns=['order_number', 'customer_number']).astype({'order_number':'Int64', 'customer_number':'Int64'})
print(largest_orders(Orders))