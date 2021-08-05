# Given the array nums, obtain a subsequence of the array whose sum of elements is strictly greater than the sum of the non included elements in such subsequence.
# If there are multiple solutions, return the subsequence with minimum size and if there still exist multiple solutions, return the subsequence with the maximum total sum of all its elements. A subsequence of an array can be obtained by erasing some (possibly zero) elements from the array.
# Note that the solution with the given constraints is guaranteed to be unique. Also return the answer sorted in non-increasing order.

def minSubsequence(nums):
    nums = sorted(nums, reverse = True)

    for indx in range(len(nums)):
        if sum(nums[:indx + 1]) > sum(nums[indx + 1:]):
            return nums[:indx + 1]

#Test cases
nums = [4,3,10,9,8]
print(minSubsequence(nums))

nums = [4,4,7,6,7]
print(minSubsequence(nums))

nums = [6]
print(minSubsequence(nums))
