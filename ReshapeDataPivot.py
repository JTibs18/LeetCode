# Write a solution to pivot the data so that each row represents temperatures for a specific month, and each city is a separate column.

import pandas as pd 

def pivotTable(weather):
    return weather.pivot(columns='city', index='month', values='temperature')

# Test cases
data = [['Jacksonville', 'January', 13],
        ['Jacksonville', 'February', 23],
        ['Jacksonville', 'March', 38], 
        ['Jacksonville', 'April', 5],
        ['Jacksonville', 'May', 34],
        ['ElPaso', 'January', 20],
        ['ElPaso', 'February', 6],
        ['ElPaso', 'March', 26], 
        ['ElPaso', 'April', 2],
        ['ElPaso', 'May', 43]]
weather = pd.DataFrame(data, columns=['city', 'month', 'temperature'])
print(pivotTable(weather))