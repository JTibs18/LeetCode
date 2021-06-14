# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

def SearchInsert(nums, target):
    for index, value in enumerate(nums):
        if target == nums[index]:
            return index
        elif target > nums[index] and (index + 1) < len(nums):
            if target < nums[index + 1]:
                return index + 1
        elif target > nums[index] and index + 1 == len(nums):
            return index + 1
        else:
            return 0

#Test cases
nums = [1, 3, 5, 6]
target = 5
print(SearchInsert(nums, target))

nums = [1, 3, 5, 6]
target = 2
print(SearchInsert(nums, target))

nums = [1, 3, 5, 6]
target = 7
print(SearchInsert(nums, target))

nums = [1, 3, 5, 6]
target = 0
print(SearchInsert(nums, target))

nums = [1]
target = 0
print(SearchInsert(nums, target))
