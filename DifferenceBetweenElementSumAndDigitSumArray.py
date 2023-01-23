# You are given a positive integer array nums.
# The element sum is the sum of all the elements in nums.
# The digit sum is the sum of all the digits (not necessarily distinct) that appear in nums.
# Return the absolute difference between the element sum and digit sum of nums.
# Note that the absolute difference between two integers x and y is defined as |x - y|.

def differenceOfSum(nums):
    elementSum = sum(nums)
    digitSum = 0 

    for i in nums: 
        if i < 10: 
            digitSum += i 
        else: 
            i = str(i)
            for digit in i: 
                digitSum += int(digit)
    
    return abs(elementSum - digitSum)

# Test cases
nums = [1,15,6,3]
print(differenceOfSum(nums))

nums = [1,2,3,4]
print(differenceOfSum(nums))
