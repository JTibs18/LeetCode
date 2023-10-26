# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

# time is o(n log n)
def longestConsecutive1(nums):
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

# time is o(n) and memory is o(n)
def longestConsecutive(nums):
    nums = set(nums)
    longestSequence = 0 

    for i in nums: 
        if (i - 1) not in nums:
            length = 0 
            while (i + length) in nums: 
                length += 1 
            longestSequence = max(length, longestSequence)
        
    return longestSequence

# Test cases
nums = [100,4,200,1,3,2]
print(longestConsecutive(nums))

nums = [0,3,7,2,5,8,4,6,0,1]
print(longestConsecutive(nums))

nums = [1,2,0,1]
print(longestConsecutive(nums))
