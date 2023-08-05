# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

import math 

# naive solution with division
def productExceptSelf1(nums):
    output = []
    result = math.prod(nums)
    
    for indx, val in enumerate(nums):
        if val == 0: 
            output.append(math.prod(nums[indx + 1:]) * math.prod(nums[:indx]))
        else: 
            output.append(result // val)

    return output

# proper solution that runs in O(n) time and uses O(1) extra space
def productExceptSelf(nums):
    output = []
    product = 1

    output.append(1)
    
    for i in range(1, len(nums)):
        product = product * nums[i - 1]
        output.append(product) 

    product = 1 

    for i in range(len(nums) - 1, -1, -1):
        output[i] = product * output[i]
        product = nums[i] * product

    return output
    
# Test cases
nums = [1,2,3,4]
print(productExceptSelf(nums))

nums = [-1,1,0,-3,3]
print(productExceptSelf(nums))
