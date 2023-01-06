# Given an array of integers nums, calculate the pivot index of this array.
# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
# Return the leftmost pivot index. If no such index exists, return -1.

# First Attempt: More space efficient than time efficent 
def pivotIndex1(nums): 
    indx = 0

    while indx < len(nums): 
        if sum(nums[:indx]) == sum(nums[indx + 1:]):
            return indx
        indx += 1 
    
    return -1

# Second Attempt: More time efficient than space efficent 
def pivotIndex(nums): 
    indx = 0
    sumLeft = 0 
    sumRight = sum(nums)

    while indx < len(nums): 
        sumRight -= nums[indx]
        if sumLeft == sumRight:
            return indx
        sumLeft += nums[indx]
        indx += 1 
    
    return -1

# Test cases 
nums = [1,7,3,6,5,6]
print(pivotIndex(nums))

nums = [1,2,3]
print(pivotIndex(nums))

nums = [2,1,-1]
print(pivotIndex(nums))

nums = [-1,-1,0,1,1,0]
print(pivotIndex(nums))
