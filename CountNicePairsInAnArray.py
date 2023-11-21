# You are given an array nums that consists of non-negative integers. Let us define rev(x) as the reverse of the non-negative integer x. For example, rev(123) = 321, and rev(120) = 21. A pair of indices (i, j) is nice if it satisfies all of the following conditions:
# 0 <= i < j < nums.length
# nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
# Return the number of nice pairs of indices. Since that number can be too large, return it modulo 109 + 7.
# With help from: https://leetcode.com/problems/count-nice-pairs-in-an-array/solutions/4311440/python3-two-sum-approach-number-of-pairs-n-n-1-2-beats-99/?envType=daily-question&envId=2023-11-21

import math 

# using n choose 2, slow runtime 
def countNicePairs1(nums):
    sumOfNumAndRev = dict()
    count = 0 

    for i in nums:
        rev = str(i)[::-1]
        sumOfNum = int(rev) - i
        
        if sumOfNum in sumOfNumAndRev:
            sumOfNumAndRev[sumOfNum] += 1
        else:
            sumOfNumAndRev[sumOfNum] = 1

    for i in sumOfNumAndRev.values():
        if i > 1: 
            count += math.factorial(i) // (math.factorial(2) * math.factorial(i - 2))
    
    return count % (10 ** 9 + 7)

# using handshake formula, fast runtime 
def countNicePairs(nums):
    sumOfNumAndRev = dict()
    count = 0 

    for i in nums:
        rev = str(i)[::-1]
        sumOfNum = int(rev) - i
        
        if sumOfNum in sumOfNumAndRev:
            sumOfNumAndRev[sumOfNum] += 1
        else:
            sumOfNumAndRev[sumOfNum] = 1

    for i in sumOfNumAndRev.values():
        if i > 1: 
            count += (i * (i - 1)) // 2
    
    return count % (10 ** 9 + 7)

# Test cases
nums = [42, 11, 1, 97]
print(countNicePairs(nums))

nums = [13, 10, 35, 24, 76]
print(countNicePairs(nums))
