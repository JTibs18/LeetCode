# Write a solution to find the number of times each student attended each exam.
# Return the result table ordered by student_id and subject_name.
# With help from https://leetcode.com/problems/students-and-examinations/solutions/3872699/pandas-vs-sql-elegant-short-all-30-days-of-pandas-solutions/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd

def students_and_examinations(students, subjects, examinations):
    return pd.merge(left=pd.merge(
        students, subjects, how='cross',
    ).sort_values(
        by=['student_id', 'subject_name']
    ),
    right=examinations.groupby(
        ['student_id', 'subject_name']
    ).agg(
        attended_exams=('subject_name', 'count')
    ).reset_index(),
    how='left',
    on=['student_id', 'subject_name']
    ).fillna(0)[['student_id', 'student_name', 'subject_name', 'attended_exams']]

# schema 
data = [[1, 'Alice'], [2, 'Bob'], [13, 'John'], [6, 'Alex']]
Students = pd.DataFrame(data, columns=['student_id', 'student_name']).astype({'student_id':'Int64', 'student_name':'object'})
data = [['Math'], ['Physics'], ['Programming']]
Subjects = pd.DataFrame(data, columns=['subject_name']).astype({'subject_name':'object'})
data = [[1, 'Math'], [1, 'Physics'], [1, 'Programming'], [2, 'Programming'], [1, 'Physics'], [1, 'Math'], [13, 'Math'], [13, 'Programming'], [13, 'Physics'], [2, 'Math'], [1, 'Math']]
Examinations = pd.DataFrame(data, columns=['student_id', 'subject_name']).astype({'student_id':'Int64', 'subject_name':'object'})
print(students_and_examinations(Students, Subjects, Examinations))