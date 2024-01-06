# You are given a 0-indexed array of integers nums.
# A prefix nums[0..i] is sequential if, for all 1 <= j <= i, nums[j] = nums[j - 1] + 1. In particular, the prefix consisting only of nums[0] is sequential.
# Return the smallest integer x missing from nums such that x is greater than or equal to the sum of the longest sequential prefix.
# For BiWeekly Contest 121 Question #1 

def missingInteger(nums):
    allNums = set(nums)
    prefixSum = nums[0]

    for i in range(1, len(nums)):
        if nums[i - 1] + 1 == nums[i]:
            prefixSum += nums[i]
        else:
            break 

    while prefixSum in allNums:
        prefixSum += 1 

    return prefixSum

# Test cases
nums = [1, 2, 3, 2, 5]
print(missingInteger(nums))

nums = [3, 4, 5, 1, 12, 14, 13]
print(missingInteger(nums))
