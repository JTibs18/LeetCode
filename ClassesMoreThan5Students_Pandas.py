# Write a solution to find all the classes that have at least five students.
# Return the result table in any order.
# With help from https://leetcode.com/problems/classes-more-than-5-students/solutions/3899196/pandas-2-liner-easy-to-understand/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd

def find_classes(courses):
    classCount = courses.groupby('class')['student'].count().reset_index()
    return classCount[classCount['student'] >= 5][['class']]

# schema
data = [['A', 'Math'], ['B', 'English'], ['C', 'Math'], ['D', 'Biology'], ['E', 'Math'], ['F', 'Computer'], ['G', 'Math'], ['H', 'Math'], ['I', 'Math']]
Courses = pd.DataFrame(data, columns=['student', 'class']).astype({'student':'object', 'class':'object'})
print(find_classes(Courses))