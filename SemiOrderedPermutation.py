# You are given a 0-indexed permutation of n integers nums.
# A permutation is called semi-ordered if the first number equals 1 and the last number equals n. You can perform the below operation as many times as you want until you make nums a semi-ordered permutation:
# Pick two adjacent elements in nums, then swap them.
# Return the minimum number of operations to make nums a semi-ordered permutation.
# A permutation is a sequence of integers from 1 to n of length n containing each number exactly once.

def semiOrderedPermutation(nums):
    lenArr = len(nums)
    lowIndx = nums.index(1)
    highIndx = nums.index(lenArr)

    if lowIndx < highIndx:
        return lowIndx + (lenArr - highIndx - 1)
    
    return lowIndx + (lenArr - highIndx - 2)

# Test cases
nums = [2, 1, 4, 3]
print(semiOrderedPermutation(nums))

nums = [2, 4, 1, 3]
print(semiOrderedPermutation(nums))

nums = [1, 3, 4, 2, 5]
print(semiOrderedPermutation(nums))
