# Given a 0-indexed integer array nums, find a 0-indexed integer array answer where:
#   answer.length == nums.length.
#   answer[i] = |leftSum[i] - rightSum[i]|.
# Where:
#   leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
#   rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.
# Return the array answer.

# faster runtime but takes more memory
def leftRightDifferences1(nums):
    leftSum = 0 
    rightSum = sum(nums)
    answer = []

    for val in nums: 
        rightSum -= val 
        answer.append(abs(rightSum - leftSum))
        leftSum += val 

    return answer

# slower runtime but takes less memory 
def leftRightDifferences(nums):
    answer = []

    for indx in range(len(nums)): 
        answer.append(abs(sum(nums[:indx]) - sum(nums[indx + 1:])))

    return answer
    
# Test cases
nums = [10,4,8,3]
print(leftRightDifferences(nums))

nums = [1]
print(leftRightDifferences(nums))
