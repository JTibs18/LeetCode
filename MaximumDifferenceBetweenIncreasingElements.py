# Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j] (i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].
# Return the maximum difference. If no such i and j exists, return -1.

def maximumDifference(nums):
    maxDiff = -1

    for i in range(1, len(nums)):
        diff = max(nums[i:]) - nums[i - 1]
        
        if diff > maxDiff and diff != 0:
            maxDiff = diff

    return maxDiff

# Test cases
nums = [7,1,5,4]
print(maximumDifference(nums))

nums = [9,4,3,2]
print(maximumDifference(nums))

nums = [1,5,2,10]
print(maximumDifference(nums))
