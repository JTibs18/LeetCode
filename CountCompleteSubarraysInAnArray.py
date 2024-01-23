# You are given an array nums consisting of positive integers.
# We call a subarray of an array complete if the following condition is satisfied:
#   The number of distinct elements in the subarray is equal to the number of distinct elements in the whole array.
# Return the number of complete subarrays.
# A subarray is a contiguous non-empty part of an array.

def countCompleteSubarrays(nums):
    uniqueNums = len(set(nums))
    totalNums = len(nums)

    def helper(start, end, curCount, curSet):
        if end == totalNums and end - start < uniqueNums:
            return curCount
        
        if end == totalNums:
            return helper(start + 1, start + uniqueNums, curCount, set(nums[start + 1:uniqueNums + start + 1]))

        curSet.add(nums[end])

        if len(curSet) == uniqueNums:
            curCount += 1 

        return helper(start, end + 1, curCount, curSet)
    
    return helper(0, uniqueNums - 1, 0, set(nums[0:uniqueNums])) 

# Test cases
nums = [1,3,1,2,2]
print(countCompleteSubarrays(nums))

nums = [5,5,5,5]
print(countCompleteSubarrays(nums))
