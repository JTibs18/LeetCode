# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.

def removeDuplicates(nums): 
    ptr1 = 0 
    ptr2 = 0
    uniqueNums = set() 

    while ptr1 < len(nums): 
        if nums[ptr1] not in uniqueNums: 
            uniqueNums.add(nums[ptr1])
            
            if nums[ptr2] == -1: 
                nums[ptr2] = nums[ptr1]
                nums[ptr1] = -1 
                ptr1 += 1 
                ptr2 += 1 
            else: 
                ptr1 += 1 
        else:  
            nums[ptr1] = -1 

            if nums[ptr2] != -1: 
                ptr2 = ptr1 
            
            ptr1 += 1 
    
    return len(uniqueNums)

# Test cases 
nums = [1, 1, 2]
print(removeDuplicates(nums))

nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))

nums = [1, 2]
print(removeDuplicates(nums))