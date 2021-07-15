# You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.
# Return the sum of all the unique elements of nums.

def sumOfUnique(nums):
    numCount = dict()
    sum = 0

    for n in nums:
        if n in numCount:
            numCount[n] += 1
        else:
            numCount[n] = 1

    for key, val in numCount.items():
        if val == 1:
            sum += key

    return sum

#Test cases
nums = [1, 2, 3, 2]
print(sumOfUnique(nums))

nums = [1,1,1,1,1]
print(sumOfUnique(nums))

nums = [1,2,3,4,5]
print(sumOfUnique(nums))
