# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:
# Input: nums = [0]
# Output: [0]

def moveZeroes(nums):
    frontp = 0
    endp = len(nums) - 1
    while frontp < len(nums):
        if (nums[frontp] == 0 and frontp < endp):
            for x in range((len(nums) - frontp) - 1):
                nums[frontp + x] = nums[frontp + 1 + x]
            nums[endp] = 0
            endp -= 1
        else:
            frontp += 1
    return(nums)

#Test cases
nums = [0,1,0,3,12]
print(moveZeroes(nums))

nums = [0]
print(moveZeroes(nums))

nums = [0, 0, 1]
print(moveZeroes(nums))
