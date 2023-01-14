# Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

def arrayPairSum(nums):
    ptr1 = 0 
    ptr2 = 1
    sum = 0

    nums = sorted(nums)
    while (ptr2 < len(nums)):
        sum += nums[ptr1]
        ptr1 += 2
        ptr2 += 2

    return sum

# Test cases
nums = [1,4,3,2]
print(arrayPairSum(nums))

nums = [6,2,6,5,1,2]
print(arrayPairSum(nums))
