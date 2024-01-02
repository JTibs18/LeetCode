# You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:
# The 2D array should contain only the elements of the array nums.
# Each row in the 2D array contains distinct integers.
# The number of rows in the 2D array should be minimal.
# Return the resulting array. If there are multiple answers, return any of them.
# Note that the 2D array can have a different number of elements on each row.

def findMatrix(nums):
    numCount = dict()
    twoDArr = []

    for i in nums:
        if i not in numCount:
            numCount[i] = 1
        else:
            numCount[i] += 1 
    
    for key, val in numCount.items():
        for i in range(val):
            if i >= len(twoDArr):
                twoDArr.append([key])
            else:
                twoDArr[i].append(key)

    return twoDArr

# Test cases
nums = [1,3,4,1,2,3,1]
print(findMatrix(nums))

nums = [1,2,3,4]
print(findMatrix(nums))
