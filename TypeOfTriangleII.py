# You are given a 0-indexed integer array nums of size 3 which can form the sides of a triangle.
# A triangle is called equilateral if it has all sides of equal length.
# A triangle is called isosceles if it has exactly two sides of equal length.
# A triangle is called scalene if all its sides are of different lengths.
# Return a string representing the type of triangle that can be formed or "none" if it cannot form a triangle.
# For Biweekly Contest #123: Question 1

def triangleType(nums):
    sideCount = dict()

    if nums[0] + nums[1] <= nums[2] or nums[1] + nums[2] <= nums[0] or nums[0] + nums[2] <= nums[1]:
        return "none"
 
    for i in nums:
        if i in sideCount:
            sideCount[i] += 1
        else:
            sideCount[i] = 1

    for val in sideCount.values():
        if val == 3:
            return "equilateral"
        elif val == 2:
            return "isosceles"
    
    return "scalene"
        
# Test cases
nums = [3, 3, 3]
print(triangleType(nums))

nums = [3, 4, 5]
print(triangleType(nums))

nums = [100, 1, 2]
print(triangleType(nums))

nums = [8, 4, 4]
print(triangleType(nums))

nums = [1, 1, 7]
print(triangleType(nums))
