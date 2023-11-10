# Write a solution to fill in the missing value as 0 in the quantity column.

import pandas as pd

def fillMissingValues(products):
    products['quantity'] = products['quantity'].fillna(0)
    return products

# Test cases
data = [['Wristwatch', None, 135], 
        ['WirelessEarbuds', None, 821],
        ['GolfClubs', 779, 9319],
        ['Printer', 849, 3051]]
products = pd.DataFrame(data, columns=['name', 'quantity', 'price'])
print(fillMissingValues(products))