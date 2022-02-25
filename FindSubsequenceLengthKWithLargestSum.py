# You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that has the largest sum.
# Return any such subsequence as an integer array of length k.
# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

def maxSubsequence(nums, k):
    newNums = sorted(nums, reverse = True) 

    for i in range(k, len(nums)):
        nums.remove((newNums[i]))

    return nums

#Test cases
nums = [2,1,3,3]
k = 2
print(maxSubsequence(nums, k))

nums = [-1,-2,3,4]
k = 3
print(maxSubsequence(nums, k))

nums = [3,4,3,3]
k = 2
print(maxSubsequence(nums, k))
