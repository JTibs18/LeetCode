# Given an array of integers called nums, you can perform any of the following operation while nums contains at least 2 elements:
#   Choose the first two elements of nums and delete them.
#   Choose the last two elements of nums and delete them.
#   Choose the first and the last elements of nums and delete them.
# The score of the operation is the sum of the deleted elements.
# Your task is to find the maximum number of operations that can be performed, such that all operations have the same score.
# Return the maximum number of operations possible that satisfy the condition mentioned above.
# For Biweekly Contest #124 Question 3

def maxOperations(nums):
    def helper(nums, maxCount, curVal, memo={}):
        if tuple(nums) in memo: 
            return memo[tuple(nums)]

        if not nums or len(nums) == 1:
            return maxCount
        
        memo[tuple(nums)] = maxCount

        if nums[0] + nums[1] == curVal:
            memo[tuple(nums)] = max(helper(nums[2:], maxCount + 1, curVal, memo), memo[tuple(nums)])
        
        if nums[0] + nums[-1] == curVal:
            memo[tuple(nums)] = max(helper(nums[1:-1], maxCount + 1, curVal, memo), memo[tuple(nums)])

        if nums[-1] + nums[-2] == curVal:
            memo[tuple(nums)] = max(helper(nums[:-2], maxCount + 1, curVal, memo), memo[tuple(nums)])

        return memo[tuple(nums)]
    
    return max(helper(nums[2:], 1, nums[0] + nums[1]), helper(nums[1:-1], 1, nums[0] + nums[-1]), helper(nums[:-2], 1, nums[-1] + nums[-2]))

# Test cases
nums = [3, 2, 1, 2, 3, 4]
print(maxOperations(nums))

nums = [3, 2, 6, 1, 4]
print(maxOperations(nums))

nums = [1,9,7,3,2,7,4,12,2,6] # 2
print(maxOperations(nums))

nums = [3,3,2,4,1,5,2,4,6,4] # 4
print(maxOperations(nums))
