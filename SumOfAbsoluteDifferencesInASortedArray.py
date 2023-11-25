# You are given an integer array nums sorted in non-decreasing order.
# Build and return an integer array result with the same length as nums such that result[i] is equal to the summation of absolute differences between nums[i] and all the other elements in the array.
# In other words, result[i] is equal to sum(|nums[i]-nums[j]|) where 0 <= j < nums.length and j != i (0-indexed).

def getSumAbsoluteDifferences(nums):
    output = []
    prefix = 0
    suffix = sum(nums)
    lenNums = len(nums)

    for indx, val in enumerate(nums):
        suffix -= val 

        left = (val * indx) - prefix 
        right = suffix - (val * (lenNums - indx - 1))
        output.append(left + right)

        prefix += val 
    
    return output

# Test cases
nums = [2, 3, 5]
print(getSumAbsoluteDifferences(nums))

nums = [1, 4, 6, 8, 10]
print(getSumAbsoluteDifferences(nums))
