# You are given a 0-indexed integer array nums. A subarray s of length m is called alternating if:
#   m is greater than 1.
#   s1 = s0 + 1.
#   The 0-indexed subarray s looks like [s0, s1, s0, s1,...,s(m-1) % 2]. In other words, s1 - s0 = 1, s2 - s1 = -1, s3 - s2 = 1, s4 - s3 = -1, and so on up to s[m - 1] - s[m - 2] = (-1)m.
# Return the maximum length of all alternating subarrays present in nums or -1 if no such subarray exists.
# A subarray is a contiguous non-empty sequence of elements within an array.

def alternatingSubarray(nums):
    count = 0 
    maxCount = 0 
    alternatingNums = []

    for i in range(1, len(nums)):
        if abs(nums[i] - nums[i - 1]) == 1 and alternatingNums and nums[i] in alternatingNums and nums[i - 1] in alternatingNums:
            count += 1 
        elif nums[i] - nums[i - 1] == 1:
            maxCount = max(maxCount, count)
            count = 2
            alternatingNums = [nums[i], nums[i - 1]]
        else:
            maxCount = max(maxCount, count)
            count = 0

    return max(maxCount, count) or -1

# Test cases
nums = [2, 3, 4, 3, 4]
print(alternatingSubarray(nums))

nums = [4, 5, 6]
print(alternatingSubarray(nums))

nums = [74,75,74,75,74,75,74,75]
print(alternatingSubarray(nums))
