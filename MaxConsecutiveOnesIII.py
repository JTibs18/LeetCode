# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

def longestOnes (nums, k):
    p1 = 0
    p2 = 0
    consecutive = 0
    flipped = 0
    maxC = 0

    if k == len(nums):
        return len(nums)
    elif sum(nums) == 0:
        return 0

    if nums[p1] == 1:
        consecutive += 1
    elif k != 0:
        consecutive += 1
        flipped += 1
    else:
        p1 += 1
        p2 += 1
    p2 += 1

    while (p2 <= len(nums) - 1 and p1 <= p2):
        if nums[p2] == 1:
            consecutive += 1
            p2 += 1
        elif flipped < k:
            consecutive += 1
            flipped += 1
            p2 += 1
        else:
            if consecutive > maxC:
                maxC = consecutive
            if nums[p1] == 0 and flipped != 0:
                flipped -= 1
            if consecutive == 0 or p1 == p2:
                p2 += 1
            else:
                consecutive -= 1
            p1 += 1

    if consecutive > maxC:
        maxC = consecutive
    return maxC

# Test cases
nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2
print(longestOnes(nums, k))

nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
print(longestOnes(nums, k))

nums = [0,0,1, 1, 1, 0, 0]
k = 0
print(longestOnes(nums, k))

nums = [1,1,1,0,0,0,1,1,1,1]
k = 0
print(longestOnes(nums, k))

nums = [0,0,0,0]
k = 0
print(longestOnes(nums, k))
