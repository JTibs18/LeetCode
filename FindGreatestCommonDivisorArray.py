# Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.
# The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

def findGCD(nums):
    smallest = min(nums)
    largest = max(nums)
    possibleGCD = smallest

    while possibleGCD: 
        if largest % possibleGCD == 0 and smallest % possibleGCD == 0: 
            return possibleGCD
        possibleGCD -= 1

# Test cases 
nums = [2,5,6,9,10]
print(findGCD(nums))

nums = [7, 5, 6, 8, 3]
print(findGCD(nums))

nums = [3, 3]
print(findGCD(nums))
