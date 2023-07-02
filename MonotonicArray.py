# An array is monotonic if it is either monotone increasing or monotone decreasing.
# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
# Given an integer array nums, return true if the given array is monotonic, or false otherwise.

def isMonotonic(nums): 
    if nums[0] - nums[len(nums) - 1] > 0: 
        direction = "dec"
    elif nums[0] - nums[len(nums) - 1] < 0: 
        direction = "inc"
    else: 
        direction = "eq"
    
    for indx in range(len(nums) - 1): 
        if direction == "dec" and nums[indx] - nums[indx + 1] < 0:
            return False 
        elif direction == "inc" and nums[indx] - nums[indx + 1] > 0: 
            return False 
        elif direction == "eq" and nums[indx] - nums[indx + 1] != 0:
            return False 

    return True  

# Test cases
nums = [1, 2, 2, 3]
print(isMonotonic(nums))

nums = [6, 5, 4, 4]
print(isMonotonic(nums))

nums = [1, 3, 2]
print(isMonotonic(nums))

nums = [1, 1, 0]
print(isMonotonic(nums))
