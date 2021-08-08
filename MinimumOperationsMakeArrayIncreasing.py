# You are given an integer array nums (0-indexed). In one operation, you can choose an element of the array and increment it by 1.
# For example, if nums = [1,2,3], you can choose to increment nums[1] to make nums = [1,3,3].
# Return the minimum number of operations needed to make nums strictly increasing.
# An array nums is strictly increasing if nums[i] < nums[i+1] for all 0 <= i < nums.length - 1. An array of length 1 is trivially strictly increasing.

def minOperations(nums):
    incr = 0

    for indx, n in enumerate(nums):
        if indx != 0 and n <= nums[indx - 1]:
            diff = nums[indx - 1] - n
            incr += diff + 1
            nums[indx] = diff + 1 + n
    return incr

#Test cases
nums = [1,1,1]
print(minOperations(nums))

nums = [1,5,2,4,1]
print(minOperations(nums))

nums = [8]
print(minOperations(nums))
