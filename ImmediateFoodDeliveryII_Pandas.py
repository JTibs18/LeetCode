# If the customer's preferred delivery date is the same as the order date, then the order is called immediate; otherwise, it is called scheduled.
# The first order of a customer is the order with the earliest order date that the customer made. It is guaranteed that a customer has precisely one first order.
# Write a solution to find the percentage of immediate orders in the first orders of all customers, rounded to 2 decimal places.

import pandas as pd 

def immediate_food_delivery(delivery):
    firstOrders = delivery.groupby(['customer_id']).min()
    immediateOrders = len(firstOrders[firstOrders['order_date'] == firstOrders['customer_pref_delivery_date']])
    return pd.DataFrame({'immediate_percentage': [round((immediateOrders / len(firstOrders) * 100), 2)]})

# Schema 
data = [[1, 1, '2019-08-01', '2019-08-02'], [2, 2, '2019-08-02', '2019-08-02'], [3, 1, '2019-08-11', '2019-08-12'], [4, 3, '2019-08-24', '2019-08-24'], [5, 3, '2019-08-21', '2019-08-22'], [6, 2, '2019-08-11', '2019-08-13'], [7, 4, '2019-08-09', '2019-08-09']]
delivery = pd.DataFrame(data, columns=['delivery_id', 'customer_id', 'order_date', 'customer_pref_delivery_date']).astype({'delivery_id':'Int64', 'customer_id':'Int64', 'order_date':'datetime64[ns]', 'customer_pref_delivery_date':'datetime64[ns]'})
print(immediate_food_delivery(delivery)) 