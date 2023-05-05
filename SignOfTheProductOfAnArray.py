# There is a function signFunc(x) that returns:
# 1 if x is positive.
# -1 if x is negative.
# 0 if x is equal to 0.
# You are given an integer array nums. Let product be the product of all values in the array nums.
# Return signFunc(product).

def arraySign(nums): 
    negativeCount = 0 

    for i in nums: 
        if i == 0: 
            return 0 
        elif i < 0: 
            negativeCount += 1 
    
    if negativeCount % 2 == 0: 
        return 1
    return -1 

# Test cases
nums = [-1,-2,-3,-4,3,2,1]
print(arraySign(nums))

nums = [1,5,0,2,-3]
print(arraySign(nums))

nums = [-1,1,-1,1,-1]
print(arraySign(nums))
