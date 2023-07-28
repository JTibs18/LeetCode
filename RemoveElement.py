# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.

def removeElement(nums, val): 
    ptr1 = 0 
    ptr2 = len(nums) - 1
    numValElements = 0 

    while ptr1 <= ptr2: 
        if nums[ptr2] == val: 
            nums[ptr2] = -1 
            ptr2 -= 1 
            numValElements += 1 
        elif nums[ptr1] == val: 
            nums[ptr1] = nums[ptr2]
            nums[ptr2] = -1 
            ptr1 += 1 
            ptr2 -= 1
            numValElements += 1 
        elif nums[ptr1] != val: 
            ptr1 += 1

    return len(nums) - numValElements

# Test cases
nums = [3, 2, 2, 3]
val = 3 
print(removeElement(nums, val))

nums = [0,1,2,2,3,0,4,2]
val = 2
print(removeElement(nums, val))

nums = [1]
val = 1 
print(removeElement(nums, val))