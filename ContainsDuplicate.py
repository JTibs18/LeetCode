# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

from collections import Counter

# Second fastest solution that has same memory as best solution
def containsDuplication(nums): 
    duplicate = set() 
    
    for i in nums: 
        duplicate.add(i)

    if len(duplicate) == len(nums): 
        return False
    return True

# Worst solution in terms of time and memory 
def containsDuplication2(nums): 
    nums = sorted(nums)
    ptr1 = 0 
    ptr2 = 1 

    while ptr2 < len(nums): 
        if nums[ptr1] == nums[ptr2]: 
            return True
        ptr1 += 1
        ptr2 += 1
        
    return False 

# Best solution in terms of speed and uses least amount of memory
def containsDuplication3(nums): 
    counter = Counter(nums)

    for i in counter.values(): 
        if i > 1: 
            return True
    
    return False
    
# Test cases
nums = [1, 2, 3, 1]
print(containsDuplication3(nums))

nums = [1,2,3,4]
print(containsDuplication3(nums))

nums = [1,1,1,3,3,4,3,2,4,2]
print(containsDuplication3(nums))
