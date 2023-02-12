# For Weekly Contest 332 Question #1

# You are given a 0-indexed integer array nums.
# The concatenation of two numbers is the number formed by concatenating their numerals.
# For example, the concatenation of 15, 49 is 1549.
# The concatenation value of nums is initially equal to 0. Perform this operation until nums becomes empty:
# If there exists more than one number in nums, pick the first element and last element in nums respectively and add the value of their concatenation to the concatenation value of nums, then delete the first and last element from nums.
# If one element exists, add its value to the concatenation value of nums, then delete it.
# Return the concatenation value of the nums.

def findTheArrayConcValue(nums): 
    indx1 = 0
    indx2 = len(nums) - 1
    concValue = 0
    
    while indx1 < indx2: 
        concValue += int(str(nums[indx1]) + str(nums[indx2]))

        indx1 += 1
        indx2 -= 1
    
    if indx1 == indx2: 
        concValue += nums[indx1]
    
    return concValue

# Test cases
nums = [7,52,2,4]
print(findTheArrayConcValue(nums))

nums = [5,14,13,8,12]
print(findTheArrayConcValue(nums))
