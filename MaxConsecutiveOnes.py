# Given a binary array nums, return the maximum number of consecutive 1's in the array.

def findMaxConOnes(nums):
    consecutive = 0
    max = 0

    for indx, val in enumerate(nums):
        if val == 0:
            if consecutive > max:
                max = consecutive
            consecutive = 0
        else:
            consecutive += 1
    if consecutive > max:
        max = consecutive
    return max 

#Test cases
nums = [1, 1, 0, 1, 1, 1]
print(findMaxConOnes(nums))

nums = [1, 0, 1, 1, 0, 1]
print(findMaxConOnes(nums))
