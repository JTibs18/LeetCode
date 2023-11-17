# The pair sum of a pair (a,b) is equal to a + b. The maximum pair sum is the largest pair sum in a list of pairs.
# For example, if we have pairs (1,5), (2,3), and (4,4), the maximum pair sum would be max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8.
# Given an array nums of even length n, pair up the elements of nums into n / 2 pairs such that:
# Each element of nums is in exactly one pair, and
# The maximum pair sum is minimized.
# Return the minimized maximum pair sum after optimally pairing up the elements.

def minPairSum(nums):
    ptr1 = 0 
    ptr2 = len(nums) - 1
    maxSum = 0

    nums.sort()

    while ptr1 < ptr2: 
        newSum = nums[ptr1] + nums[ptr2]
        
        if newSum > maxSum:
            maxSum = newSum
        
        ptr1 += 1
        ptr2 -= 1 

    return maxSum

# Test cases
nums = [3, 5, 2, 3]
print(minPairSum(nums))

nums = [3, 5, 4, 2, 4, 6]
print(minPairSum(nums))
