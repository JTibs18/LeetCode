# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

def findDissappearedNumbers(nums): 
    foundNums = set() 
    missingNums = []
    
    for i in nums: 
        foundNums.add(i) 
    
    for i in range(1, len(nums) + 1): 
        if i not in foundNums: 
            missingNums.append(i)

    return missingNums

# Test cases
nums = [4,3,2,7,8,2,3,1]
print(findDissappearedNumbers(nums))

nums = [1,1]
print(findDissappearedNumbers(nums))
