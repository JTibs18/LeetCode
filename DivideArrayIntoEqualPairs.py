# You are given an integer array nums consisting of 2 * n integers.
# You need to divide nums into n pairs such that:
# Each element belongs to exactly one pair.
# The elements present in a pair are equal.
# Return true if nums can be divided into n pairs, otherwise return false.

def divideArray(nums): 
    numCount = dict()

    for i in nums: 
        if i in numCount: 
            numCount[i] += 1
        else:
            numCount[i] = 1 

    for val in numCount.values(): 
        if val % 2 != 0: 
            return False 
    
    return True 

# Test cases
nums = [3,2,3,2,2,2]
print(divideArray(nums))

nums = [1,2,3,4]
print(divideArray(nums))
