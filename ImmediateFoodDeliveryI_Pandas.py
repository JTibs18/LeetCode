# If the customer's preferred delivery date is the same as the order date, then the order is called immediate; otherwise, it is called scheduled.
# Write a solution to find the percentage of immediate orders in the table, rounded to 2 decimal places.

import pandas as pd

def food_delivery(delivery): 
    allOrders = len(delivery)
    immediateOrders = len(delivery[delivery['order_date'] == delivery['customer_pref_delivery_date']])
    return pd.DataFrame({'immediate_percentage': [round((immediateOrders / allOrders) * 100, 2)]})

# schema
data = [[1, 1, '2019-08-01', '2019-08-02'], [2, 5, '2019-08-02', '2019-08-02'], [3, 1, '2019-08-11', '2019-08-11'], [4, 3, '2019-08-24', '2019-08-26'], [5, 4, '2019-08-21', '2019-08-22'], [6, 2, '2019-08-11', '2019-08-13']]
Delivery = pd.DataFrame(data, columns=['delivery_id', 'customer_id', 'order_date', 'customer_pref_delivery_date']).astype({'delivery_id':'Int64', 'customer_id':'Int64', 'order_date':'datetime64[ns]', 'customer_pref_delivery_date':'datetime64[ns]'})
print(food_delivery(Delivery))