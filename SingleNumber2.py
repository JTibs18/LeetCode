# Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

#O(n) time and O(n) space (faster runtime, less memory efficient)
def singleNumber2(nums):
    nCount = dict()

    for n in nums:
        if n not in nCount:
            nCount[n] = 1
        else:
            nCount[n] += 1

    for key, val in nCount.items():
        if val == 1:
            return key

#O(n) time and O(1) space (slower runtime, more memory efficient)
def singleNumber22(nums):
    nums.sort()

    if len(nums) == 1:
        return nums[0]

    if nums[0] != nums[1]:
        return nums[0]
    elif nums[-1] != nums[-2]:
        return nums[-1]

    i = 0
    while i < len(nums) - 1:
        if nums[i] != nums[i + 1]:
            return nums[i]
        i += 3

#Test cases
nums = [2,2,3,2]
print(singleNumber2(nums))
print(singleNumber22(nums))

nums = [0,1,0,1,0,1,99]
print(singleNumber2(nums))
print(singleNumber22(nums))
