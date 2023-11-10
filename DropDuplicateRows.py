# There are some duplicate rows in the DataFrame based on the email column.
# Write a solution to remove these duplicate rows and keep only the first occurrence.

import pandas as pd

def dropDuplicateEmails(customers): 
    return customers.drop_duplicates('email') 

# Test cases
data = [[1, 'Ella', 'emily@example.com'], 
        [2, 'David', 'michael@eample.com'],
        [3, 'Zachary', 'sarah@example.com'],
        [4, 'Alice', 'john@example.com'], 
        [5, 'Finn', 'john@example.com'],
        [6, 'Violet', 'alice@example.com']]
customers = pd.DataFrame(data, columns=['customer_id', 'name', 'email'])
print(dropDuplicateEmails(customers))