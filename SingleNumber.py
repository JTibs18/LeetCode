# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

def singleNumber(nums):
    nCount = dict()

    for n in nums:
        if n not in nCount:
            nCount[n] = 1
        else:
            nCount[n] += 1

    for key, val in nCount.items():
        if val == 1:
            return key

#Test cases
nums = [2, 2, 1]
print(singleNumber(nums))

nums = [4, 1, 2, 1, 2]
print(singleNumber(nums))

nums = [1]
print(singleNumber(nums))
