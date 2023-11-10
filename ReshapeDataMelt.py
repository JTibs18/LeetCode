# Write a solution to reshape the data so that each row represents sales data for a product in a specific quarter.

import pandas as pd

def meltTable(report): 
    return pd.melt(report, id_vars='product', value_vars=['quarter_1', 'quarter_2', 'quarter_3', 'quarter_4'], value_name='sales', var_name='quarter')
    
# Test cases
data = [['Umbrella', 417, 224, 379, 611],
        ['SleepingBag', 800, 936, 93, 875]]
report = pd.DataFrame(data, columns=['product', 'quarter_1', 'quarter_2', 'quarter_3', 'quarter_4'])
print(meltTable(report))