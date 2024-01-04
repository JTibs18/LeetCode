# You are given a 0-indexed integer array nums. The array nums is beautiful if:
#   nums.length is even.
#   nums[i] != nums[i + 1] for all i % 2 == 0.
# Note that an empty array is considered beautiful.
# You can delete any number of elements from nums. When you delete an element, all the elements to the right of the deleted element will be shifted one unit to the left to fill the gap created and all the elements to the left of the deleted element will remain unchanged.
# Return the minimum number of elements to delete from nums to make it beautiful.

# naive approach: very slow 
def minDeletion1(nums):
    indx = 0
    deleteCount = 0 

    while indx < len(nums) - 1:
        if indx % 2 == 0 and nums[indx] == nums[indx + 1]:
            deleteCount += 1 
            del nums[indx]
        else:        
            indx += 1

    if len(nums) % 2 != 0:
        deleteCount += 1

    return deleteCount 

# stack: much faster solution
def minDeletion(nums):
    stack = []

    for i in nums:
        if not(stack and len(stack) % 2 != 0 and i == stack[-1]) or not stack:
            stack.append(i)

    if len(stack) % 2 == 0:
        return len(nums) - len(stack)
    
    return len(nums) - len(stack) + 1

# Test cases
nums = [1, 1, 2, 3, 5]
print(minDeletion(nums))

nums = [1, 1, 2, 2, 3, 3]
print(minDeletion(nums))

nums = [0,1,5,4,2,4,7,2,3,0,3,0,0,9,7,5,9,4,3,9,9,2,1,6,3,1,0,7,6,6,6,0,1,7,1,9,4,9,3,3,4,5,0,3,8,7,1,8,4,5]
print(minDeletion(nums))
