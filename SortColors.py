# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.

def sortColors(nums): 
    ptr1 = 0
    ptr2 = len(nums) - 1
    curIndx = 0

    while curIndx <= ptr2:
        if nums[curIndx] == 0: 
            temp = nums[curIndx]
            nums[curIndx] = nums[ptr1]
            nums[ptr1] = temp 
            ptr1 += 1
            curIndx += 1 
        elif nums[curIndx] == 2: 
            temp = nums[ptr2]
            nums[ptr2] = nums[curIndx]
            nums[curIndx] = temp 
            ptr2 -= 1 
        else: 
            curIndx += 1 

    return nums

# Test cases
nums = [2, 0, 2, 1, 1, 0]
print(sortColors(nums))

nums = [2, 0, 1]
print(sortColors(nums))
