# Write a solution to fix the names so that only the first character is uppercase and the rest are lowercase.
# Return the result table ordered by user_id.

import pandas as pd 

# slower solution that uses more memory 
def fix_names1(users): 
    for i in users.index:
        users.at[i, 'name'] = users['name'][i].capitalize()
    
    return users.sort_values(by=['user_id'])

# better solution, faster and uses less memory 
def fix_names(users):
    users['name'] = users['name'].str.capitalize()
    return users.sort_values(by=['user_id'])

# schema 
data = [[1, 'aLice'], [2, 'bOB']]
Users = pd.DataFrame(data, columns=['user_id', 'name']).astype({'user_id':'Int64', 'name':'object'})
print(fix_names(Users))