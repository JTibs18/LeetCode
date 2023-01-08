# For Weekly Contest #327 Problem #1 

# Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.
# In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, then return the maximum of pos and neg.
# Note that 0 is neither positive nor negative.

def maximumCount(nums):
    positiveCount = 0 
    negativeCount = 0 

    for i in nums: 
        if i > 0: 
            positiveCount += 1
        elif i < 0: 
            negativeCount += 1 
    
    return max(positiveCount, negativeCount)

# Test cases
nums = [-2,-1,-1,1,2,3]
print(maximumCount(nums))

nums = [-3,-2,-1,0,0,1,2]
print(maximumCount(nums))

nums = [5,20,66,1314]
print(maximumCount(nums))