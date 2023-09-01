# A single number is a number that appeared only once in the MyNumbers table.
# Find the largest single number. If there is no single number, report null.

import pandas as pd

def biggest_single_number(my_numbers):
    return my_numbers.drop_duplicates(keep=False).max().to_frame(name='num')

# schema
data = [[8], [8], [3], [3], [1], [4], [5], [6]]
MyNumbers = pd.DataFrame(data, columns=['num']).astype({'num':'Int64'})
print(biggest_single_number(MyNumbers))