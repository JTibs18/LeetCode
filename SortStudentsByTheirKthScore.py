# For Weekly Contest #329 Question #2
# There is a class with m students and n exams. You are given a 0-indexed m x n integer matrix score, where each row represents one student and score[i][j] denotes the score the ith student got in the jth exam. The matrix score contains distinct integers only.
# You are also given an integer k. Sort the students (i.e., the rows of the matrix) by their scores in the kth (0-indexed) exam from the highest to the lowest.
# Return the matrix after sorting it.

def sortTheStudents(score, k): 
    score = sorted(score, key=lambda x: x[k], reverse=True)
    return score 

# Test cases
score = [[10,6,9,1],[7,5,11,2],[4,8,3,15]]
k = 2
print(sortTheStudents(score, k))

score = [[3,4],[5,6]]
k = 0
print(sortTheStudents(score, k))
