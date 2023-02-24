# You are given a 0-indexed integer array nums and a target element target.
# A target index is an index i such that nums[i] == target.
# Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. The returned list must be sorted in increasing order.

def targetIndices(nums, target): 
    targetIndex = []
    nums = sorted(nums)
    l = 0
    r = len(nums) 
    lowestMatchIndex = ''

    while l < r: 
        mid = l + (r - l) // 2
        if nums[mid] == target:
            r = mid
            lowestMatchIndex = mid 
        elif nums[mid] < target: 
            l = mid + 1 
        else: 
            r = mid
    
    if lowestMatchIndex != '': 
        while lowestMatchIndex < len(nums) and nums[lowestMatchIndex] == target: 
            targetIndex.append(lowestMatchIndex)
            lowestMatchIndex += 1 

    return targetIndex

# Test cases
nums = [1, 2, 5, 2, 3]
target = 2
print(targetIndices(nums, target))

nums = [1, 2, 5, 2, 3]
target = 3 
print(targetIndices(nums, target))

nums = [1, 2, 5, 2, 3]
target = 5
print(targetIndices(nums, target))

nums = [100, 1, 100]
target = 100 
print(targetIndices(nums, target))
