# You are given a 0-indexed integer array nums. In one operation, you may do the following:
# Choose two integers in nums that are equal.
# Remove both integers from nums, forming a pair.
# The operation is done on nums as many times as possible.
# Return a 0-indexed integer array answer of size 2 where answer[0] is the number of pairs that are formed and answer[1] is the number of leftover integers in nums after doing the operation as many times as possible.
import math 

def numberOfPairs(nums): 
    numCount = dict() 
    leftOvers = 0 
    pairs = 0 

    for i in nums: 
        if i in numCount: 
            numCount[i] += 1
        else: 
            numCount[i] = 1 
    
    for value in numCount.values(): 
        leftOvers += value % 2 
        pairs += math.floor(value / 2)

    return [pairs, leftOvers]

# Test cases
nums = [1,3,2,1,3,2,2]
print(numberOfPairs(nums))

nums = [1,1]
print(numberOfPairs(nums))

nums = [0]
print(numberOfPairs(nums))
