# Given a binary array nums, you should delete one element from it.
# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

def longestSubarray(nums): 
    oneSections = []
    oneCount = 0 
    ptr1 = 0 
    longestSequence = 0 

    for i in nums: 
        if i == 1: 
            oneCount += 1
        else:
            oneSections.append(oneCount)
            oneCount = 0 
    oneSections.append(oneCount)
    
    if len(oneSections) == 1 and 0 not in nums: 
        return oneSections[0] - 1
    elif len(oneSections) == 1: 
        return oneSections[0]
    
    while ptr1 < len(oneSections) - 1: 
        if oneSections[ptr1] + oneSections[ptr1 + 1] > longestSequence: 
            longestSequence = oneSections[ptr1] + oneSections[ptr1 + 1]
        ptr1 += 1

    return longestSequence

# Test cases
nums = [1, 1, 0, 1]
print(longestSubarray(nums))

nums = [0,1,1,1,0,1,1,0,1]
print(longestSubarray(nums))

nums = [1,1,1]
print(longestSubarray(nums))
