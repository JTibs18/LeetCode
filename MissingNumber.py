# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

def missingNumber(nums): 
    nums = sorted(nums)
    l = 0 
    r = len(nums)

    while l < r: 
        mid = (l + (r - 1)) // 2
        if mid == nums[mid]:
            l = mid + 1 
        else: 
            r = mid

    if (l == len(nums)): 
        return mid + 1
    
    return l
        
# Test cases
nums = [3,0,1]
print(missingNumber(nums))

nums = [0,1]
print(missingNumber(nums))

nums = [9,6,4,2,3,5,7,0,1]
print(missingNumber(nums))

nums = [1, 2, 3]
print(missingNumber(nums))

nums = [0, 2, 3]
print(missingNumber(nums))
