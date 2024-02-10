# Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.
# Return the positive integer k. If there is no such integer, return -1.

# naive solution 
def findMaxK1(nums):
    numCount = dict()

    for i in nums:
        absVal = abs(i)
        if absVal not in numCount:
            numCount[absVal] = set([i])
        else:
            numCount[absVal].add(i)

    for i in sorted(numCount.keys())[::-1]:
        if len(numCount[i]) == 2:
            return i 
    
    return -1

# two pointer solution 
def findMaxK(nums):
    ptr1 = 0
    ptr2 = len(nums) - 1
    nums.sort()

    while ptr1 < ptr2:
        absVal = abs(nums[ptr1])
        if absVal == nums[ptr2] and nums[ptr1] != nums[ptr2]:
            return absVal
        
        if absVal > nums[ptr2]:
            ptr1 += 1 
        else:
            ptr2 -= 1 
    
    return -1

# Test cases
nums = [-1, 2, -3, 3]
print(findMaxK(nums))

nums = [-1, 10, 6, 7, -7, 1]
print(findMaxK(nums))

nums = [-10, 8, 6, 7, -2, -3]
print(findMaxK(nums))
