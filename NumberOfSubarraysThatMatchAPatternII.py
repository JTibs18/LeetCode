# You are given a 0-indexed integer array nums of size n, and a 0-indexed integer array pattern of size m consisting of integers -1, 0, and 1.
# A subarray nums[i..j] of size m + 1 is said to match the pattern if the following conditions hold for each element pattern[k]:
# nums[i + k + 1] > nums[i + k] if pattern[k] == 1.
# nums[i + k + 1] == nums[i + k] if pattern[k] == 0.
# nums[i + k + 1] < nums[i + k] if pattern[k] == -1.
# Return the count of subarrays in nums that match the pattern.
# With help from https://www.youtube.com/watch?v=JoF0Z7nVSrA

def countMatchingSubarrays(nums, pattern): 
    numsPattern = []
    count = 0 
    lps = [0] * len(pattern)
    prevLPS, indx = 0, 1
    indxNumsPattern = 0  
    indxPattern = 0   

    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            numsPattern.append(0)
        elif nums[i + 1] > nums[i]: 
            numsPattern.append(1)
        else:
            numsPattern.append(-1)

    # longest prefix suffix (LPS)
    while indx < len(pattern):
        if pattern[indx] == pattern[prevLPS]:
            lps[indx] = prevLPS + 1
            prevLPS += 1
            indx += 1 
        elif prevLPS == 0:
            lps[indx] = 0 
            indx += 1 
        else:
            prevLPS = lps[prevLPS - 1]

    # Knuth Morris Pratt (KMP) algorithm 
    while indxNumsPattern < len(numsPattern):
        if numsPattern[indxNumsPattern] == pattern[indxPattern]:
            indxNumsPattern += 1
            indxPattern += 1
        elif indxPattern == 0:
            indxNumsPattern += 1 
        else:
            indxPattern = lps[indxPattern - 1]

        if indxPattern == len(pattern):
            indxPattern = lps[indxPattern - 1]
            count += 1 
            
    return count     

# Test cases
nums = [1,2,3,4,5,6]
pattern = [1,1]
print(countMatchingSubarrays(nums, pattern))

nums = [1,4,4,1,3,5,5,3]
pattern = [1,0,-1]
print(countMatchingSubarrays(nums, pattern))
