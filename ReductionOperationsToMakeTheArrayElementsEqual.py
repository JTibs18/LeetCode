# Given an integer array nums, your goal is to make all elements in nums equal. To complete one operation, follow these steps:
# 1. Find the largest value in nums. Let its index be i (0-indexed) and its value be largest. If there are multiple elements with the largest value, pick the smallest i.
# 2. Find the next largest value in nums strictly smaller than largest. Let its value be nextLargest.
# 3. Reduce nums[i] to nextLargest.
# Return the number of operations to make all elements in nums equal.

def reductionOperations(nums): 
    operationCount = 0 
    nums.sort(reverse=True)

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            operationCount += i

    return operationCount

# Test cases
nums = [5, 1, 3]
print(reductionOperations(nums))

nums = [1, 1, 1]
print(reductionOperations(nums))

nums = [1, 1, 2, 2, 3]
print(reductionOperations(nums))