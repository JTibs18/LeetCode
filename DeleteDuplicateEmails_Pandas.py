# Write a solution to delete all duplicate emails, keeping only one unique email with the smallest id.
# For Pandas users, please note that you are supposed to modify Person in place.
# After running your script, the answer shown is the Person table. The driver will first compile and run your piece of code and then show the Person table. The final order of the Person table does not matter.

import pandas as pd

def delete_duplicate_emails(person):
    person.sort_values(by=['id'], inplace=True)
    person.drop_duplicates(subset=['email'], inplace=True)
    print(person)

# schema 
data = [[1, 'john@example.com'], [2, 'bob@example.com'], [3, 'john@example.com']]
Person = pd.DataFrame(data, columns=['id', 'email']).astype({'id':'int64', 'email':'object'})
delete_duplicate_emails(Person)