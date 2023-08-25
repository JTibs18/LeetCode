# Write a solution to calculate the number of bank accounts for each salary category. The salary categories are:
#   "Low Salary": All the salaries strictly less than $20000.
#   "Average Salary": All the salaries in the inclusive range [$20000, $50000].
#   "High Salary": All the salaries strictly greater than $50000.
# The result table must contain all three categories. If there are no accounts in a category, return 0.
# Return the result table in any order.

import pandas as pd

def count_salary_categories(accounts):
    salary_count = []

    salary_count.append((accounts['income'] < 20000).sum())
    salary_count.append(((accounts['income'] >= 20000) & (accounts['income'] <= 50000)).sum())
    salary_count.append((accounts['income'] > 50000).sum())

    return pd.DataFrame({'category': ['Low Salary', 'Average Salary', 'High Salary'], 'accounts_count': salary_count})

# schema
data = [[3, 108939], [2, 12747], [8, 87709], [6, 91796]]
Accounts = pd.DataFrame(data, columns=['account_id', 'income']).astype({'account_id':'Int64', 'income':'Int64'})
print(count_salary_categories(Accounts))