# Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).

def maxProduct(nums):
    n1 = max(nums)
    nums.remove(n1)
    n2 = max(nums)
    return (n1 - 1) * (n2 - 1) 

#Test cases
nums = [3, 4, 5, 2]
print(maxProduct(nums))

nums = [1, 5, 4, 5]
print(maxProduct(nums))

nums = [3, 7]
print(maxProduct(nums))
