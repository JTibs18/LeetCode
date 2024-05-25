# You are given an array nums, where each number in the array appears either once or twice.
# Return the bitwise XOR of all the numbers that appear twice in the array, or 0 if no number appears twice.
# For Biweekly Contest #131 Question 1

from collections import Counter  

def duplicateNumbersXOR_V1(nums):
        numCount = {}
        dups = []
        
        for i in nums:
            if i in numCount:
                numCount[i] += 1
            else: 
                numCount[i] = 1 
        
        for key, val in numCount.items(): 
            if val > 1: 
                dups.append(key)
        
        if len(dups) > 0: 
            xorTotal = dups[0]
        
            for x in dups[1:]:
                xorTotal ^= x
                
            return xorTotal
        return 0

def duplicateNumbersXOR(nums):
    numCount = Counter(nums)
    duplicateNums = []

    for key, value in numCount.items():
        if value > 1:
            duplicateNums.append(key)

    if len(duplicateNums) > 0: 
        xorTotal = duplicateNums[0]

        for x in duplicateNums[1:]:
            xorTotal ^= x
            
        return xorTotal
    return 0

# Test cases
nums = [1, 2, 1, 3]
print(duplicateNumbersXOR(nums))

nums = [1, 2, 3]
print(duplicateNumbersXOR(nums))

nums = [1, 2, 2, 1]
print(duplicateNumbersXOR(nums))
