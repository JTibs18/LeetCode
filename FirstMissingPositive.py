# Given an unsorted integer array nums, return the smallest missing positive integer.
# You must implement an algorithm that runs in O(n) time and uses constant extra space.

# Note: question does not indicate that there can be duplicate numbers but there can be, hence converting array to set

def firstMissingPositive(nums): 
    nums = sorted(set(nums))
    smallestNum = 0
    
    for i in nums: 
        if i > 0: 
            smallestNum += 1 
            if smallestNum != i: 
                return smallestNum
    
    return smallestNum + 1 

# Test cases
nums = [1, 2, 0]
print(firstMissingPositive(nums))

nums = [3, 4, -1, 1]
print(firstMissingPositive(nums))

nums = [7, 8, 9, 11, 12]
print(firstMissingPositive(nums))

nums = [0, 2, 2, 1, 1]
print(firstMissingPositive(nums))
