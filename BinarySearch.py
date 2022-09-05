# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.

def search(nums, target):
    ptr1 = 0
    ptr2 = len(nums) - 1

    while ptr1 <= ptr2:
        if nums[ptr1] == target:
            return ptr1

        if nums[ptr2] == target:
            return ptr2

        ptr1 += 1
        ptr2 -= 1

    return -1

#Test Cases
nums = [-1,0,3,5,9,12]
target = 9
print(search(nums, target))

nums = [-1,0,3,5,9,12]
target = 2
print(search(nums, target))

nums = [5]
target = 5
print(search(nums, target))
