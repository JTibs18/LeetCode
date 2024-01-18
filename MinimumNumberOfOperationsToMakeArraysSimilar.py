# You are given two positive integer arrays nums and target, of the same length.
# In one operation, you can choose any two distinct indices i and j where 0 <= i, j < nums.length and:
#   set nums[i] = nums[i] + 2 and
#   set nums[j] = nums[j] - 2.
# Two arrays are considered to be similar if the frequency of each element is the same.
# Return the minimum number of operations required to make nums similar to target. The test cases are generated such that nums can always be similar to target.

def makeSimilar(nums, target):
    nums.sort()
    target.sort()
    count = 0 
    numsOdd = []
    numsEven = []
    targetOdd = []
    targetEven = []

    for indx, val in enumerate(nums):
        if val % 2 == 0:
            numsEven.append(val)
        else:
            numsOdd.append(val)

        if target[indx] % 2 == 0:
            targetEven.append(target[indx])
        else:
            targetOdd.append(target[indx])

    for i in range(len(numsEven)):
        diff = abs(numsEven[i] - targetEven[i])
        if diff != 0:
            count += diff // 2

    for i in range(len(numsOdd)):
        diff = abs(numsOdd[i] - targetOdd[i])
        if diff != 0:
            count += diff // 2

    return count // 2

# Test cases
nums = [8, 12, 6]
target = [2, 14, 10]
print(makeSimilar(nums, target))

nums = [1, 2, 5]
target = [4, 1, 3]
print(makeSimilar(nums, target))

nums = [1, 1, 1, 1, 1]
target = [1, 1, 1, 1, 1]
print(makeSimilar(nums, target))
