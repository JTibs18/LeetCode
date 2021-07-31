# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
# Return the answer in an array.

def smallerNumbersThanCurrent(nums):
    ans = []
    s = sorted(nums)

    for i in nums:
        ans.append(s.index(i))
    return ans

#Test Cases
nums = [8,1,2,2,3]
print(smallerNumbersThanCurrent(nums))

nums = [6,5,4,8]
print(smallerNumbersThanCurrent(nums))

nums = [7,7,7,7]
print(smallerNumbersThanCurrent(nums))
