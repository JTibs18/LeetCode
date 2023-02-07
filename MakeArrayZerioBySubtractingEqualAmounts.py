# You are given a non-negative integer array nums. In one operation, you must:
# Choose a positive integer x such that x is less than or equal to the smallest non-zero element in nums.
# Subtract x from every positive element in nums.
# Return the minimum number of operations to make every element in nums equal to 0.

def minimumOperations(nums):
    operationCount = 0 

    while True:
        nums = [i for i in nums if i != 0]
        
        if len(nums) == 0: 
            break 

        subtract = min(nums) 
        
        for indx, val in enumerate(nums):
            nums[indx] = val - subtract 
        operationCount += 1 
    
    return operationCount
        

# Test cases
nums = [1,5,0,3,5]
print(minimumOperations(nums))

nums = [0]
print(minimumOperations(nums))
