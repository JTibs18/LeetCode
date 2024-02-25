# You are given an integer array nums of even length. You have to split the array into two parts nums1 and nums2 such that:
#   nums1.length == nums2.length == nums.length / 2.
#   nums1 should contain distinct elements.
#   nums2 should also contain distinct elements.
# Return true if it is possible to split the array, and false otherwise.
# For Weekly Contest #386 Question 1

def isPossibleToSplit(nums):
    numCount = dict()
    ones = 0 

    for i in nums:
        if i in numCount:
            numCount[i] += 1
        else:
            numCount[i] = 1 

    for values in numCount.values():
        if values > 2: 
            return False 
        elif values == 1: 
            ones += 1 

    if ones % 2 == 0:
        return True 
    return False

# Test cases
nums = [1,1,2,2,3,4]
print(isPossibleToSplit(nums))

nums = [1,1,1,1]
print(isPossibleToSplit(nums))
