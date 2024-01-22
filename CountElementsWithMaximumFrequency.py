# You are given an array nums consisting of positive integers.
# Return the total frequencies of elements in nums such that those elements all have the maximum frequency.
# The frequency of an element is the number of occurrences of that element in the array.

def maxFrequencyElements(nums):
    numCount = dict()
    maxNums = 0 

    for i in nums:
        if i in numCount:
            numCount[i] += 1
        else:
            numCount[i] = 1

    maxVal = max(numCount.values())

    for val in numCount.values():
        if maxVal == val:
            maxNums += val

    return maxNums

# Test cases
nums = [1, 2, 2, 3, 1, 4]
print(maxFrequencyElements(nums))

nums = [1, 2, 3, 4, 5]
print(maxFrequencyElements(nums))
