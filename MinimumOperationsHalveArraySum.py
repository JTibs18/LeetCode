# You are given an array nums of positive integers. In one operation, you can choose any number from nums and reduce it to exactly half the number. (Note that you may choose this reduced number in future operations.)
# Return the minimum number of operations to reduce the sum of nums by at least half.
import heapq

def halveArray(nums): 
    nums = [-num for num in nums]
    heapq.heapify(nums)
        
    count = 0 
    half = sum(nums) / 2 
    removedAmount = 0
    
    while (removedAmount > half): 
        count += 1 
        highestNum = heapq.heappop(nums)
        removedAmount += highestNum / 2
        heapq.heappush(nums, highestNum / 2)
    
    return count

# Test cases
nums = [5,19,8,1]
print(halveArray(nums))

nums = [3,8,20]
print(halveArray(nums))
