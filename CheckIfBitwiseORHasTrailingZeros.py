# You are given an array of positive integers nums.
# You have to check if it is possible to select two or more elements in the array such that the bitwise OR of the selected elements has at least one trailing zero in its binary representation.
# For example, the binary representation of 5, which is "101", does not have any trailing zeros, whereas the binary representation of 4, which is "100", has two trailing zeros.
# Return true if it is possible to select two or more elements whose bitwise OR has trailing zeros, return false otherwise.
# For Weekly Contest 378 Question #1

def hasTrailingZeros(nums):
    trailingZeroCount = 0 

    for i in nums:
        if bin(i)[2:].zfill(8)[-1] == "0":
            trailingZeroCount += 1
        
    if trailingZeroCount >= 2: 
        return True
    return False

# Test cases
nums = [1,2,3,4,5]
print(hasTrailingZeros(nums))

nums = [2,4,8,16]
print(hasTrailingZeros(nums))

nums = [1,3,5,7,9]
print(hasTrailingZeros(nums))
