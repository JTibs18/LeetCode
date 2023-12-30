# You are given an array nums consisting of positive integers.
# You have to take each integer in the array, reverse its digits, and add it to the end of the array. You should apply this operation to the original integers in nums.
# Return the number of distinct integers in the final array.

def countDistinctIntegers(nums):
    n = set(nums)

    for i in nums:
        n.add(int(str(i)[::-1]))
    
    return len(n)

# Test cases
nums = [1,13,10,12,31]
print(countDistinctIntegers(nums))

nums = [2,2,2]
print(countDistinctIntegers(nums))
