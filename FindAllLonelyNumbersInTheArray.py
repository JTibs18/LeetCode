# You are given an integer array nums. A number x is lonely when it appears only once, and no adjacent numbers (i.e. x + 1 and x - 1) appear in the array.
# Return all lonely numbers in nums. You may return the answer in any order.

def findLonely(nums): 
    numCount = dict()
    lonelyNumbers = []

    for i in nums: 
        if i in numCount:
            numCount[i] += 1
        else: 
            numCount[i] = 1 
    
    uniqueNums = {k: v for (k, v) in numCount.items() if v == 1}

    for i in uniqueNums: 
        if not ((i - 1 in numCount.keys()) or (i + 1 in numCount.keys())): 
            lonelyNumbers.append(i)

    return lonelyNumbers

# Test cases
nums = [10,6,5,8]
print(findLonely(nums))

nums = [1,3,5,3]
print(findLonely(nums))

nums = [75,35,59,66,69,53,37,16,60,98,11,33,3,85,59,65,59,44,34,89,72,47]
print(findLonely(nums))