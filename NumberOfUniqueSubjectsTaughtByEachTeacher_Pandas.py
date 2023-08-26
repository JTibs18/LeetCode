# Write a solution to calculate the number of unique subjects each teacher teaches in the university.
# Return the result table in any order.
# second function with help from https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/solutions/3899157/pandas-very-straight-forward-approach-easy-to-understand/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd 

def count_unique_subjects1(teacher): 
    teacher = teacher.groupby(['teacher_id', 'subject_id']).sum().reset_index()
    teacher = teacher.groupby('teacher_id')['dept_id'].size().reset_index()
    return teacher.rename(columns={'dept_id': 'cnt'})

def count_unique_subjects(teacher): 
    teacher = teacher.groupby('teacher_id')['subject_id'].nunique().reset_index() 
    return teacher.rename(columns={'subject_id':'cnt'})

# schema
data = [[1, 2, 3], [1, 2, 4], [1, 3, 3], [2, 1, 1], [2, 2, 1], [2, 3, 1], [2, 4, 1]]
Teacher = pd.DataFrame(data, columns=['teacher_id', 'subject_id', 'dept_id']).astype({'teacher_id':'Int64', 'subject_id':'Int64', 'dept_id':'Int64'})
print(count_unique_subjects(Teacher))