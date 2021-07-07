# Given an n x n matrix where each of the rows and columns are sorted in ascending order, return the kth smallest element in the matrix.
# Note that it is the kth smallest element in the sorted order, not the kth distinct element.

def kthSmallest(matrix, k):
    nums = []
    for i in matrix:
        nums.extend(i)
    nums.sort()
    return nums[k - 1]

#Test Cases
matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
k = 8
print(kthSmallest(matrix, k))

matrix = [[-5]]
k = 1
print(kthSmallest(matrix, k))
