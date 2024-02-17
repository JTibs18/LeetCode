# Given an array of integers called nums, you can perform the following operation while nums contains at least 2 elements:
#   Choose the first two elements of nums and delete them.
# The score of the operation is the sum of the deleted elements.
# Your task is to find the maximum number of operations that can be performed, such that all operations have the same score.
# Return the maximum number of operations possible that satisfy the condition mentioned above.
# For Biweekly Contest #124 Question 1

def maxOperations(nums):
    operationCount = 0
    nums = nums[::-1]
    curSum = float("inf")

    while len(nums) >= 2:
        if curSum == float('inf'):
            curSum = nums.pop() + nums.pop()
            operationCount += 1 
        else:
            newSum = nums.pop() + nums.pop()
            if newSum == curSum:
                operationCount += 1
            else:
                break 

    return operationCount

# Test cases
nums = [3, 2, 1, 4, 5]
print(maxOperations(nums))

nums = [3, 2, 6, 1, 4]
print(maxOperations(nums))
