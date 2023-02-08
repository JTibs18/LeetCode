# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:
# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

def jump(nums):
    stepCounter = 0
    indx = 0 

    if len(nums) == 1: 
        return 0 

    while indx < len(nums) - 1: 
        maxSteps = 0
        newIndx = indx 

        for i in range(indx + 1, indx + 1 + nums[indx]):
            if i >= len(nums) - 1:
                newIndx = i 
                break 
            elif i + nums[i] > maxSteps: 
                maxSteps = i + nums[i]
                newIndx = i 
        indx = newIndx
        stepCounter += 1  

    return stepCounter

# Test cases
nums = [2,3,1,1,4]
print(jump(nums))

nums = [2,3,0,1,4]
print(jump(nums))

nums = [0]
print(jump(nums))

nums = [1, 2]
print(jump(nums))

nums = [1,1,1,1]
print(jump(nums))
