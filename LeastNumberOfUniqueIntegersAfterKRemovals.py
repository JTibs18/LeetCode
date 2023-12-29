# Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

def findLeastNumOfUniqueInts(arr, k):
    numCount = dict()
    removeCount = 0 

    for i in arr:
        if i not in numCount:
            numCount[i] = 1 
        else:
            numCount[i] += 1 

    numCount = sorted(numCount.values())
    
    for value in numCount:
        if value <= k:
            k -= value 
            removeCount += 1 
    
    return len(numCount) - removeCount

# Test cases
arr = [5,5,4]
k = 1
print(findLeastNumOfUniqueInts(arr, k))

arr = [4,3,1,1,3,3,2]
k = 3
print(findLeastNumOfUniqueInts(arr, k))
