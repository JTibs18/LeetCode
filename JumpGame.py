# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.

# dynamic and greedy solution inspired by this video: https://leetcode.com/problems/jump-game/solutions/3222715/best-solution-explained-with-illustration/

# naive solution
def canJump1(nums): 
        indx = 0 

        if len(nums) == 1: 
            return True 

        while indx < len(nums) - 1: 
            maxSteps = 0
            if nums[indx] == 0: 
                return False

            for i in range(indx + 1, indx + 1 + nums[indx]):
                if i >= len(nums) - 1:
                    return True  
                elif i + nums[i] > maxSteps: 
                    maxSteps = i + nums[i]
                    indx = i 

        return True

# second best solution: dynamic programming
def canJump2(nums): 
    reached = [False for i in range(len(nums))]
    reached[0] = True 

    for indx, val in enumerate(nums):
        if reached[len(reached) - 1] == True: 
            return True 
        if reached[indx] == True: 
            if indx + val >= len(nums): 
                return True 
            for i in range(val): 
                reached[indx + i + 1] = True
    return False

# fastest solution: greedy 
def canJump(nums): 
    i = 0 
    maxReach = 0 
    lenNums = len(nums)

    while i < lenNums and i <= maxReach: 
        maxReach = max(maxReach, nums[i] + i)
        i += 1 
    
    return i == lenNums
    
# Test cases 
nums = [2, 3, 1, 1, 4]
print(canJump(nums))

nums = [3, 2, 1, 0, 4]
print(canJump(nums))

nums = [0, 1]
print(canJump(nums))

nums = [2, 5, 0, 0]
print(canJump(nums))

nums = [2, 0]
print(canJump(nums))

nums = [1, 0, 2]
print(canJump(nums))