# Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

import itertools 

# naive solution 
def findDifferentBinaryStringV1(nums):
    for i in itertools.product('01', repeat=len(nums[0])):
        newNum = ''.join(i)
        if newNum not in nums:
            return str(newNum)
        
# flipping a bit at every position because len(nums) == len(nums[i])
# faster solution 
def findDifferentBinaryString(nums):
    newNum = ""

    for i in range(len(nums)):
        if nums[i][i] == "0":
            newNum += "1"
        else:
            newNum += "0"

    return newNum

# Test cases
nums = ["01", "10"]
print(findDifferentBinaryString(nums))

nums = ["00", "01"]
print(findDifferentBinaryString(nums))

nums = ["111", "011", "001"]
print(findDifferentBinaryString(nums))
