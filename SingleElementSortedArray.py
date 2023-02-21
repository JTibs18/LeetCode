# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.
# Return the single element that appears only once.
# Your solution must run in O(log n) time and O(1) space.

def singleNonDuplicate(nums): 
    ptr1 = 0
    ptr2 = 1

    if len(nums) < 2:
        return nums[0]
     
    while ptr2 < len(nums): 
        if nums[ptr1] != nums[ptr2]:
            return nums[ptr1]
            
        ptr1 += 2
        ptr2 += 2
    
    return nums[len(nums) - 1]

# Test cases
nums = [1,1,2,3,3,4,4,8,8]
print(singleNonDuplicate(nums))

nums = [3,3,7,7,10,11,11]
print(singleNonDuplicate(nums))

nums = [1]
print(singleNonDuplicate(nums))

nums = [1, 1, 2]
print(singleNonDuplicate(nums))
