# Given an array of integers nums.
# A pair (i,j) is called good if nums[i] == nums[j] and i < j.
# Return the number of good pairs.

def numIdenticalPairs(nums):
    count = 0
    if len(nums) < 2:
        return 0
    p1 = 0
    p2 = 1
    while p1 < len(nums) - 1:
        if nums[p1] == nums[p2]:
            count += 1
        if p2 == len(nums) - 1:
            p1 += 1
            p2 = p1 + 1
        else:
            p2 += 1
    return count

#Test cases
nums = [1, 2, 3, 1, 1, 3]
print(numIdenticalPairs(nums))

nums = [1, 1, 1, 1]
print(numIdenticalPairs(nums))

nums = [1, 2, 3]
print(numIdenticalPairs(nums))
