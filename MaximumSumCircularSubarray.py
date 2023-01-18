# Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.
# A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].
# A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

def maxSubarraySumCircular(nums): 
    totalSum = sum(nums)
    maxSum = totalSum
    curSum = 0
    maxSubarraySum = 0

    for i in nums: 
        curSum += i 
        maxSum = max(maxSum, curSum)
        if curSum < 0:
            curSum = 0

    curSum = 0

    for i in nums: 
        maxSum = max(maxSum, (totalSum - curSum) + maxSubarraySum)
        curSum += i 
        maxSubarraySum = max(maxSubarraySum, curSum)

    return maxSum
        
# Test cases
nums = [1,-2,3,-2]
print(maxSubarraySumCircular(nums))

nums = [5,-3,5]
print(maxSubarraySumCircular(nums))

nums = [-3,-2,-3]
print(maxSubarraySumCircular(nums))
