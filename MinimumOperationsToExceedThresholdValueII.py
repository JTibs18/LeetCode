# You are given a 0-indexed integer array nums, and an integer k.
# In one operation, you will:
#   Take the two smallest integers x and y in nums.
#   Remove x and y from nums.
#   Add min(x, y) * 2 + max(x, y) anywhere in the array.
# Note that you can only apply the described operation if nums contains at least two elements.
# Return the minimum number of operations needed so that all elements of the array are greater than or equal to k.
# For Biweekly Contest #125 Question 2

import heapq

def minOperations(nums, k):
    heapq.heapify(nums)
    count = 0 

    while nums[0] < k and len(nums) > 1:
        count += 1
        num1 = heapq.heappop(nums)
        num2 = heapq.heappop(nums)
        newNum = (num1 * 2) + num2
        heapq.heappush(nums, newNum)

    return count 

# Test cases
nums = [2, 11, 10, 1, 3]
k = 10 
print(minOperations(nums, k))

nums = [1,1,2,4,9]
k = 20
print(minOperations(nums, k))
