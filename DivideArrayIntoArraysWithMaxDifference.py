# You are given an integer array nums of size n and a positive integer k.
# Divide the array into one or more arrays of size 3 satisfying the following conditions:
# Each element of nums should be in exactly one array.
# The difference between any two elements in one array is less than or equal to k.
# Return a 2D array containing all the arrays. If it is impossible to satisfy the conditions, return an empty array. And if there are multiple answers, return any of them.
# Question 2 for Weekly Contest 376

def divideArray(nums, k):
    dividedArr = []
    curArray = []
    nums.sort(reverse=True)

    for i in nums:
        if len(curArray) == 0 or curArray[0] - i <= k:
            curArray.append(i)
        else:
            return []
        
        if len(curArray) == 3:
            dividedArr.append(curArray)
            curArray = []
    
    return dividedArr

# Test cases
nums = [1,3,4,8,7,9,3,5,1]
k = 2
print(divideArray(nums, k))

nums = [1, 3, 3, 2, 7, 3]
k = 3
print(divideArray(nums, k))

nums = [33,26,4,18,16,24,24,15,8,18,34,20,24,16,3]
k = 16
print(divideArray(nums, k))
