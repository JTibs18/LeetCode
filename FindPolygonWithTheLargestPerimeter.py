# You are given an array of positive integers nums of length n.
# A polygon is a closed plane figure that has at least 3 sides. The longest side of a polygon is smaller than the sum of its other sides.
# Conversely, if you have k (k >= 3) positive real numbers a1, a2, a3, ..., ak where a1 <= a2 <= a3 <= ... <= ak and a1 + a2 + a3 + ... + ak-1 > ak, then there always exists a polygon with k sides whose lengths are a1, a2, a3, ..., ak.
# The perimeter of a polygon is the sum of lengths of its sides.
# Return the largest possible perimeter of a polygon whose sides can be formed from nums, or -1 if it is not possible to create a polygon.
# For biweekly contest #120 Question 2

def largestPerimeter(nums):
    nums.sort()
    ptr = len(nums) - 1
    left = sum(nums[:ptr])
    right = nums[ptr]

    while left <= right and ptr > 1:
        ptr -= 1
        left -= nums[ptr]
        right = nums[ptr]
        
    if ptr == len(nums) - 1 and left > right:
        return left + right
    if ptr <= 2 and right >= left:
        return -1
    return left + right

# Test cases
nums = [5,5,5]
print(largestPerimeter(nums))

nums = [1,12,1,2,5,50,3]
print(largestPerimeter(nums))

nums = [5,5,50]
print(largestPerimeter(nums)) # -1

nums = [1, 1, 2]
print(largestPerimeter(nums)) # -1

nums = [1, 2, 4]
print(largestPerimeter(nums)) # -1

nums = [1, 5, 1, 5]
print(largestPerimeter(nums)) # 12 

nums = [1, 5, 1, 7]
print(largestPerimeter(nums)) # -1

nums = [50, 12, 2, 3, 4]
print(largestPerimeter(nums)) # 9
