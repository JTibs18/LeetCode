# You are given a 1-indexed integer array nums of length n.
# An element nums[i] of nums is called special if i divides n, i.e. n % i == 0.
# Return the sum of the squares of all special elements of nums.

def sumOfSquare(nums):
    numSum = 0
    lenNums = len(nums)

    for indx in range(1, lenNums + 1):
        if lenNums % indx == 0:
            numSum += nums[indx - 1] ** 2

    return numSum

# Test cases
nums = [1, 2, 3, 4]
print(sumOfSquare(nums))

nums = [2, 7, 1, 19, 18, 3]
print(sumOfSquare(nums))
