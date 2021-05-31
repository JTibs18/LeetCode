# Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

def addUp (nums, target):
    checkedVal = {}
    for index, val in enumerate(nums):
        remain = target - val
        if remain in checkedVal.keys():
            return [checkedVal[remain], index]
        checkedVal[val] = index

#Test cases
arr1 = [2, 7, 11, 15]
target = 9
print("indexes: ", addUp(arr1, target))

arr2 = [3, 2, 4]
target = 6
print("indexes: ", addUp(arr2, target))

arr3 = [3,3]
target = 6
print("indexes: ", addUp(arr3, target))
