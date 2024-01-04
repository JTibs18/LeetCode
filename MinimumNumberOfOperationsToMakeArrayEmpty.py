# You are given a 0-indexed array nums consisting of positive integers.
# There are two types of operations that you can apply on the array any number of times:
# Choose two elements with equal values and delete them from the array.
# Choose three elements with equal values and delete them from the array.
# Return the minimum number of operations required to make the array empty, or -1 if it is not possible.

def minOperations(nums):
    count = 0 
    numCount = dict()

    for i in nums:
        if i not in numCount:
            numCount[i] = 1 
        else:
            numCount[i] += 1

    for values in numCount.values():
        if values % 3 == 0:
            count += values // 3
        elif values % 3 == 1 and values > 3:
            count += ((values - 4) // 3) + 2
        elif values % 3 == 2:
            count += (values // 3) + 1
        else:
            return -1
    
    return count

# Test cases
nums = [2,3,3,2,2,4,2,3,4]
print(minOperations(nums))

nums = [2,1,2,2,3,3]
print(minOperations(nums))

nums = [14,12,14,14,12,14,14,12,12,12,12,14,14,12,14,14,14,12,12]
print(minOperations(nums))
