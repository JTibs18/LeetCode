# Given an array nums of non-negative integers, return an array consisting of all the even elements of nums, followed by all the odd elements of nums.
# You may return any answer array that satisfies this condition.

def sortArrayByParity(nums):
    even = []
    odds = []

    for i in nums:
        if i % 2 == 0:
            even.append(i)
        else:
            odds.append(i)
    even.extend(odds)
    return even

#Test cases
nums = [3,1,2,4]
print(sortArrayByParity(nums))
