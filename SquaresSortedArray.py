# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

def sortedSquares(nums):
    squared = []

    for i in nums:
        squared.append(i ** 2)

    return sorted(squared)

#Test cases
nums = [-4, -1, 0, 3, 10]
print(sortedSquares(nums))

nums = [-7, -3, 2, 3, 11]
print(sortedSquares(nums))
