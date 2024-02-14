# You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.
# You should rearrange the elements of nums such that the modified array follows the given conditions:
# Every consecutive pair of integers have opposite signs.
# For all integers with the same sign, the order in which they were present in nums is preserved.
# The rearranged array begins with a positive integer.
# Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

def rearrangeArray(nums):
    posArr = []
    negArr = []
    newArr = []
    ptr = 0

    for i in nums:
        if i > 0:
            posArr.append(i)
        else:
            negArr.append(i)

    while ptr < len(nums) // 2:
        newArr.append(posArr[ptr])
        newArr.append(negArr[ptr])
        ptr += 1 

    return newArr

# Test cases
nums = [3, 1, -2, -5, 2, -4]
print(rearrangeArray(nums))

nums = [-1, 1]
print(rearrangeArray(nums))
