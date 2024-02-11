# You are given a 0-indexed integer array nums of size n, and a 0-indexed integer array pattern of size m consisting of integers -1, 0, and 1.
# A subarray nums[i..j] of size m + 1 is said to match the pattern if the following conditions hold for each element pattern[k]:
# nums[i + k + 1] > nums[i + k] if pattern[k] == 1.
# nums[i + k + 1] == nums[i + k] if pattern[k] == 0.
# nums[i + k + 1] < nums[i + k] if pattern[k] == -1.
# Return the count of subarrays in nums that match the pattern.
# For Weekly Contest #384 Question 2 

def countMatchingSubarrays(nums, pattern):
    ptr1 = 0 
    ptr2 = len(pattern)
    lp = len(pattern)
    patternCount = 0 

    while ptr2 < len(nums):
        curCount = 0 

        for indx, val in enumerate(pattern):
            curNode = nums[ptr1 + indx]
            nextNode = nums[ptr1 + indx + 1]
            
            if (val == 0 and nextNode == curNode) or (val == 1 and nextNode > curNode) or (val == -1 and nextNode < curNode):
                curCount += 1 
            else:
                break 

        if curCount == lp:
            patternCount += 1 
    
        ptr1 += 1
        ptr2 += 1 
        
    return patternCount

# Test cases
nums = [1,2,3,4,5,6]
pattern = [1,1]
print(countMatchingSubarrays(nums, pattern))

nums = [1,4,4,1,3,5,5,3]
pattern = [1,0,-1]
print(countMatchingSubarrays(nums, pattern))

