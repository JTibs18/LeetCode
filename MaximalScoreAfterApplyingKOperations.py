# For Weekly Contest #327 Problem #2

# You are given a 0-indexed integer array nums and an integer k. You have a starting score of 0.
# In one operation:
# choose an index i such that 0 <= i < nums.length,
# increase your score by nums[i], and
# replace nums[i] with ceil(nums[i] / 3).
# Return the maximum possible score you can attain after applying exactly k operations.
# The ceiling function ceil(val) is the least integer greater than or equal to val.

import math
import heapq

def maxKelements(nums, k): 
    score = 0 
    nums = [-num for num in nums]
    heapq.heapify(nums)

    while k: 
        largest = heapq.heappop(nums)
        print(largest)
        score += largest
        heapq.heappush(nums, math.floor(largest / 3))
        k -= 1 

    return -1 * score

# Test cases
nums = [10,10,10,10,10] 
k = 5
print(maxKelements(nums, k))

nums = [1,10,3,3,3]
k = 3
print(maxKelements(nums, k))
