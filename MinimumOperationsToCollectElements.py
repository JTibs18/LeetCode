# You are given an array nums of positive integers and an integer k.
# In one operation, you can remove the last element of the array and add it to your collection.
# Return the minimum number of operations needed to collect elements 1, 2, ..., k.

# find ways to do this faster and with less space 

def minOperations(nums, k):
    indxOfNum = dict()
    smallestIndx = len(nums)

    for indx, val in enumerate(nums):
        if val in indxOfNum: 
            indxOfNum[val].append(indx)
        else: 
            indxOfNum[val] = [indx]

    for i in range(1, k + 1): 
        curSmallest = max(indxOfNum[i]) 

        if curSmallest < smallestIndx: 
            smallestIndx = curSmallest
    
    return len(nums) - smallestIndx

# Test cases
nums = [3, 1, 5, 4, 2]
k = 2 
print(minOperations(nums, k))

nums = [3, 1, 5, 4, 2]
k = 5
print(minOperations(nums, k))

nums = [3, 2, 5, 3, 1]
k = 3
print(minOperations(nums, k))
