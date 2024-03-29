# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
# In place with O(1) extra space! 

def rotate(nums, k): 
    ptr1 = 0 
    ptr2 = 0
    count = len(nums) - 1

    while count: 
        ptr1 += k 

        if ptr1 >= len(nums): 
            ptr1 = ptr1 % len(nums)

        if ptr1 == ptr2: 
            ptr2 += 1
            ptr1 = ptr2 
            count -= 1
            continue 

        temp = nums[ptr2] 
        nums[ptr2] = nums[ptr1]
        nums[ptr1] = temp 

        count -= 1
    
    print(nums)

# Test cases
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate(nums, k)

nums = [-1, -100, 3, 99]
k = 2
rotate(nums, k)

nums = [1, 2, 3, 4, 5, 6]
k = 11
rotate(nums, k)