# Given a 0-indexed integer array nums of length n and an integer target, return the number of pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j] < target.

def countPairs(nums, target): 
    ptr1 = 0 
    ptr2 = 1
    count = 0 

    while ptr1 < len(nums) - 1: 
        if nums[ptr1] + nums[ptr2] < target: 
            count += 1 
        
        ptr2 += 1 

        if ptr2 == len(nums):
            ptr1 += 1 
            ptr2 = ptr1 + 1 
    
    return count

# Test cases
nums = [-1, 1, 2, 3, 1]
target = 2
print(countPairs(nums, target))

nums = [-6,2,5,-2,-7,-1,3]
target = -2
print(countPairs(nums, target))
