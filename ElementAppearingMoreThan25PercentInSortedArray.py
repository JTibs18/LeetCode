# Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

def findSpecialInteger(arr):
    numCount = dict()
    lenArr = len(arr)

    for i in arr:
        if i in numCount:
            numCount[i] += 1
        else:
            numCount[i] = 1
    
    for key, values in numCount.items():
        if values / lenArr > 0.25:
            return key

# Test cases
arr = [1,2,2,6,6,6,6,7,10]
print(findSpecialInteger(arr))

arr = [1,1]
print(findSpecialInteger(arr))
