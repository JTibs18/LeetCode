# Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.
# A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).

def buildArray(nums):
    ans = []

    for n in range(len(nums)):
        ans.append(nums[nums[n]])

    return ans

#Test cases
nums = [0, 2, 1, 5, 3, 4]
print(buildArray(nums))

nums = [5, 0, 1, 2, 3, 4]
print(buildArray(nums))
