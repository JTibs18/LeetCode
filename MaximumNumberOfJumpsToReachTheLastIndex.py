# You are given a 0-indexed array nums of n integers and an integer target.
# You are initially positioned at index 0. In one step, you can jump from index i to any index j such that:
#   0 <= i < j < n
#   -target <= nums[j] -= targe =  nums[i] t
# Return the maximum number of jumps you can make to reach index n - 1.
# If there is no way to reach index n - 1, return -1.

def maximumJumps(nums, target):
    maxJumps = [-1 for _ in range(len(nums))]
    maxJumps[-1] = 0

    for indx in range(len(nums) - 2, -1, -1):
        for j in range(indx + 1, len(nums)):
            if abs(nums[j] - nums[indx]) <= target and maxJumps[j] != -1:
                maxJumps[indx] = max(maxJumps[indx], maxJumps[j] + 1)
    
    return maxJumps[indx]

# # Test cases
nums = [1,3,6,4,1,2]
target = 2
print(maximumJumps(nums, target))

nums = [1,3,6,4,1,2]
target = 3
print(maximumJumps(nums, target))

nums = [1,3,6,4,1,2]
target = 0
print(maximumJumps(nums, target))

nums = [1, 0, 2] 
target = 1
print(maximumJumps(nums, target))

nums = [1, 0, 2, 3]
target = 1 
print(maximumJumps(nums, target))

nums = [0, 2, 1, 3]
target = 1 
print(maximumJumps(nums, target))
