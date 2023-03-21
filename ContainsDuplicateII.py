# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

def containsNearbyDuplicate(nums, k): 
    numsDict = dict() 

    for indx, val in enumerate(nums):
        if val in numsDict and abs(numsDict[val] - indx) <= k:
            return True 
        else:
            numsDict[val] = indx
    
    return False

# Test cases
nums = [1,2,3,1] 
k = 3
print(containsNearbyDuplicate(nums, k))

nums = [1,0,1,1] 
k = 1
print(containsNearbyDuplicate(nums, k))

nums = [1,2,3,1,2,3]
k = 2
print(containsNearbyDuplicate(nums, k))
