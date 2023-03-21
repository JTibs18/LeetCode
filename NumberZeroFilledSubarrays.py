# Given an integer array nums, return the number of subarrays filled with 0.
# A subarray is a contiguous non-empty sequence of elements within an array.

def zeroFilledSubarray(nums):
    totalZero = 0 
    countZero = 0 

    for i in nums: 
        if i == 0: 
            countZero += 1 
            totalZero += countZero
        else: 
            countZero = 0
        
    return totalZero

# Test cases
nums = [1,3,0,0,2,0,0,4]
print(zeroFilledSubarray(nums))

nums = [0,0,0,2,0,0]
print(zeroFilledSubarray(nums))

nums = [2,10,2019]
print(zeroFilledSubarray(nums))
