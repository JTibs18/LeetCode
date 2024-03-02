# You are given a 0-indexed integer array nums, and an integer k.
# In one operation, you can remove one occurrence of the smallest element of nums.
# Return the minimum number of operations needed so that all elements of the array are greater than or equal to k.
# For Biweekly Contest #125 Question 1

def minOperations(nums, k):
    count = 0 

    for i in nums: 
        if i < k: 
            count += 1 

    return count

# Test cases
nums = [2, 11, 10, 1, 3]
k = 10 
print(minOperations(nums, k))

nums = [1, 1, 2, 4, 9]
k = 1
print(minOperations(nums, k))

nums = [1, 1, 2, 4, 9]
k = 9 
print(minOperations(nums, k))
