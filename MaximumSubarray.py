# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

def maxSubarray(nums):
    max = sum(nums)

    def helperFun(nums, max, index):
        if index >= len(nums):
            return max
        if nums[index] > sum(nums[:index + 1]):
            if max < nums[index]:
                max = nums[index]
            return helperFun(nums[index:], max, 1)
        elif max < sum(nums[:index + 1]):
            max = sum(nums[:index + 1])
        return helperFun(nums, max, index + 1)

    if len(nums) > 1:
        return helperFun(nums, max, 0)
    else:
        return sum(nums)

#Test Cases
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubarray(nums))

nums = [1]
print(maxSubarray(nums))

nums = [5, 4, -1, 7, 8]
print(maxSubarray(nums))

nums = [-2, 1]
print(maxSubarray(nums))

nums = [-2, -3, -1]
print(maxSubarray(nums))
