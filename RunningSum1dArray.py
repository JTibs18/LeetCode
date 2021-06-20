# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.

def runningSum(nums):
    sum = []
    for index, val in enumerate(nums):
        if index - 1 >= 0:
            newNum = val + sum[index - 1]
        else:
            newNum = val
        sum.append(newNum)
    return sum

#Test cases
nums = [1,2,3,4]
print(runningSum(nums))
