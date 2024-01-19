# You are given a 0-indexed array nums consisting of positive integers.
# You can do the following operation on the array any number of times:
# Choose an integer i such that 0 <= i < nums.length - 1 and nums[i] <= nums[i + 1]. Replace the element nums[i + 1] with nums[i] + nums[i + 1] and delete the element nums[i] from the array.
# Return the value of the largest element that you can possibly obtain in the final array.

def maxArrayValue(nums):
    i = len(nums) - 2
    
    while i >= 0:
        if nums[i] <= nums[i + 1]:
            nums[i + 1] += nums[i]
            nums.pop(i)
            if i + 1 >= len(nums):
                i -= 1
        else:
            i -= 1

    return nums[i + 1]

# Test cases
nums = [2,3,7,9,3]
print(maxArrayValue(nums))

nums = [5,3,3]
print(maxArrayValue(nums))