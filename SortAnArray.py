# Given an array of integers nums, sort the array in ascending order and return it.
# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

# Reference: https://www.geeksforgeeks.org/merge-sort/

def sortArray(nums): 
    if len(nums) > 1: 
        mid = len(nums) // 2

        leftSide = nums[:mid]
        rightSide = nums[mid:]

        sortArray(leftSide)
        sortArray(rightSide)

        indxL = 0 
        indxR = 0 
        indxNums = 0 

        while indxL < len(leftSide) and indxR < len(rightSide): 
            if leftSide[indxL] <= rightSide[indxR]:
                nums[indxNums] = leftSide[indxL]
                indxL += 1 
            else: 
                nums[indxNums] = rightSide[indxR]
                indxR += 1 
            indxNums += 1 

        while indxL < len(leftSide): 
            nums[indxNums] = leftSide[indxL]
            indxL += 1
            indxNums += 1 

        while indxR < len(rightSide): 
            nums[indxNums] = rightSide[indxR]
            indxR += 1 
            indxNums += 1 

    return nums

# Test cases
nums = [5,2,3,1]
print(sortArray(nums))

nums = [5,1,1,2,0,0]
print(sortArray(nums))
