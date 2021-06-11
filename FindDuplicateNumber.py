# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and uses only constant extra space.

def findDuplicate(nums):
    passedNums = set()
    for index, value in enumerate(nums):
        if value in passedNums:
            return value
        else:
            passedNums.add(value)

#Test cases
nums = [1, 3, 4, 2, 2]
print(findDuplicate(nums))

nums = [3, 1, 3, 4, 2]
print(findDuplicate(nums))

nums = [1, 1]
print(findDuplicate(nums))

nums = [1, 1, 2]
print(findDuplicate(nums))
