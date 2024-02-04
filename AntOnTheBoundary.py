# An ant is on a boundary. It sometimes goes left and sometimes right.
# You are given an array of non-zero integers nums. The ant starts reading nums from the first element of it to its end. At each step, it moves according to the value of the current element:
#   If nums[i] < 0, it moves left by -nums[i] units.
#   If nums[i] > 0, it moves right by nums[i] units.
# Return the number of times the ant returns to the boundary.
# Notes:
#   There is an infinite space on both sides of the boundary.
#   We check whether the ant is on the boundary only after it has moved |nums[i]| units. In other words, if the ant crosses the boundary during its movement, it does not count.
# For Weekly Contest #383, Question 1
 
def returnToBoundaryCount(nums):
    boundary = 0 
    onBoundCount = 0 
    
    for i in nums:
        boundary += i

        if boundary == 0:
            onBoundCount += 1 

    return onBoundCount

# Test cases
nums = [2,3,-5]
print(returnToBoundaryCount(nums))

nums = [3,2,-3,-4]
print(returnToBoundaryCount(nums))
