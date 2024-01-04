# Given an array nums of integers, return how many of them contain an even number of digits.

def findNumbers(nums):
    evenNumDigitCount = 0

    for i in nums:
        if len(str(i)) % 2 == 0:
            evenNumDigitCount += 1
    
    return evenNumDigitCount

# Test cases
nums = [12,345,2,6,7896]
print(findNumbers(nums))

nums = [555,901,482,1771]
print(findNumbers(nums))
