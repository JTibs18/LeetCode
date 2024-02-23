# You are given a 0-indexed integer array nums. A pair of indices i, j where 0 <= i < j < nums.length is called beautiful if the first digit of nums[i] and the last digit of nums[j] are coprime.
# Return the total number of beautiful pairs in nums.
# Two integers x and y are coprime if there is no integer greater than 1 that divides both of them. In other words, x and y are coprime if gcd(x, y) == 1, where gcd(x, y) is the greatest common divisor of x and y.

import math 

def countBeautifulPairs(nums):
    ptr1 = 0
    ptr2 = 1
    count = 0 
    
    nums = [str(x) for x in nums]
    num1 = int(nums[ptr1][0])

    while ptr1 < len(nums) - 1:
        if math.gcd(num1, int(nums[ptr2][-1])) == 1:
            count += 1 
        
        ptr2 += 1
        
        if ptr2 == len(nums):
            ptr1 += 1
            num1 = int(nums[ptr1][0])
            ptr2 = ptr1 + 1 

    return count

# Test cases
nums = [2,5,1,4]
print(countBeautifulPairs(nums))

nums = [11,21,12]
print(countBeautifulPairs(nums))

nums = [31,25,72,79,74]
print(countBeautifulPairs(nums))
