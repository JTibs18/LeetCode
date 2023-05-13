# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

def majorityElement(nums): 
    appearMin = len(nums) // 3 
    numCount = dict() 
    output = []

    for i in nums: 
        if i in numCount: 
            numCount[i] += 1 
        else: 
            numCount[i] = 1 
    
    for key, value in numCount.items(): 
        if value > appearMin: 
            output.append(key)
        
    return output

# Test cases
nums = [3, 2, 3]
print(majorityElement(nums))

nums = [1]
print(majorityElement(nums))

nums = [1, 2]
print(majorityElement(nums))
