# You are given a 0-indexed integer array nums and an integer k.
# Return an integer that denotes the sum of elements in nums whose corresponding indices have exactly k set bits in their binary representation.
# The set bits in an integer are the 1's present when it is written in binary.
#   For example, the binary representation of 21 is 10101, which has 3 set bits.

def sumIndicesWithKSetBits(nums, k):
    setBits = []
    total = 0
    
    for i in range(len(nums)):
        if i == 0:
            setBits.append(0)
        elif i == 1:
            setBits.append(1)
        elif i % 2:
            setBits.append(setBits[i // 2] + 1)
        else:
            setBits.append(setBits[i // 2])
    
        if setBits[-1] == k:
            total += nums[i] 
        
    return total

# Test cases
nums = [5,10,1,5,2]
k = 1
print(sumIndicesWithKSetBits(nums, k))

nums = [4,3,2,1]
k = 2
print(sumIndicesWithKSetBits(nums, k))
