# Given a 0-indexed integer array nums, return the smallest index i of nums such that i mod 10 == nums[i], or -1 if such index does not exist.
# x mod y denotes the remainder when x is divided by y.

def smallestEqual(nums): 
    indx = 0 

    for val in nums: 
        if indx % 10 == val: 
            return indx
        
        indx += 1 

    return -1 

# Test cases
nums = [0, 1, 2]
print(smallestEqual(nums))

nums = [4, 3, 2, 1]
print(smallestEqual(nums))

nums = [1,2,3,4,5,6,7,8,9,0]
print(smallestEqual(nums))
