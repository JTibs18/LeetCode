# You are given a 0-indexed array of distinct integers nums.
# There is an element in nums that has the lowest value and an element that has the highest value. We call them the minimum and maximum respectively. Your goal is to remove both these elements from the array.
# A deletion is defined as either removing an element from the front of the array or removing an element from the back of the array.
# Return the minimum number of deletions it would take to remove both the minimum and maximum element from the array.

def minimumDeletions(nums):
    maxNum = float("-inf")
    minNum = float("inf")

    for val in nums:
        if val < minNum:
            minNum = val
        if val > maxNum: 
            maxNum = val
      
    minIndx = nums.index(minNum)
    maxIndx = nums.index(maxNum)

    minFromBack = len(nums) - minIndx
    maxFromBack = len(nums) - maxIndx

    delFrontAndBack = min(minIndx + 1, minFromBack) + min(maxIndx + 1, maxFromBack)
    delFront = max(minIndx, maxIndx) + 1
    delBack = max(minFromBack, maxFromBack)

    return min(delFront, delFrontAndBack, delBack)

# Test cases
nums = [2,10,7,5,4,1,8,6]
print(minimumDeletions(nums))

nums = [0,-4,19,1,8,-2,-3,5]
print(minimumDeletions(nums))

nums = [101]
print(minimumDeletions(nums))
