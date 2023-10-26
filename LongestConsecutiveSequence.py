# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

def longestConsecutive(nums):
    nums = list(set(nums))
    nums.sort()
    longestSequence = 0 
    sequenceCount = 0 
    ptr1 = 0 

    if len(nums) == 0: 
        return 0 

    while ptr1 < len(nums) - 1:
        if nums[ptr1 + 1] - 1 == nums[ptr1]: 
            sequenceCount += 1 
        elif sequenceCount > longestSequence: 
            longestSequence = sequenceCount
            sequenceCount = 0 
        else: 
            sequenceCount = 0 
        
        ptr1 += 1 

    if sequenceCount > longestSequence:
        longestSequence = sequenceCount

    return longestSequence + 1 

# Test cases
nums = [100,4,200,1,3,2]
print(longestConsecutive(nums))

nums = [0,3,7,2,5,8,4,6,0,1]
print(longestConsecutive(nums))

nums = [1,2,0,1]
print(longestConsecutive(nums))
