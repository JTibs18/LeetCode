# You are given a 0-indexed integer array nums and an integer k. Your task is to perform the following operation exactly k times in order to maximize your score:
#   Select an element m from nums.
#   Remove the selected element m from the array.
#   Add a new element with a value of m + 1 to the array.
#   Increase your score by m.
# Return the maximum score you can achieve after performing the operation exactly k times.

# slower and uses more memory 
def maximizeSum1(nums, k):
    maxSum = 0 
    maxNum = max(nums)

    for _ in range(k): 
        maxSum += maxNum
        maxNum += 1 

    return maxSum

# faster and uses less memory
def maximizeSum(nums, k):
    return k * max(nums) + k * (k - 1) // 2

# Test cases
nums = [1, 2, 3, 4, 5]
k = 3
print(maximizeSum(nums, k))

nums = [5, 5, 5]
k = 2
print(maximizeSum(nums, k))