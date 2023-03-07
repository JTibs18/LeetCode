# Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.
# Return the kth positive integer that is missing from this array.

# naive solution: uses less memory but is slower 
def findKthPositive1(arr, k): 
    num = 0
    indx = 0
    lengthArr = len(arr)

    while k > 0: 
        num += 1 

        if indx < lengthArr and num == arr[indx]:
            indx += 1
        else: 
            k -= 1

    return num 

# binary search solution: uses more memory but runs faster
def findKthPositive(arr, k): 
    leftPtr = 0 
    rightPtr = len(arr) - 1
    
    while leftPtr <= rightPtr: 
        midPtr = (leftPtr + rightPtr) // 2 
        missingNums = arr[midPtr] - midPtr - 1

        if missingNums < k: 
            leftPtr = midPtr + 1 
        else: 
            rightPtr = midPtr - 1 

    midPtr = (leftPtr + rightPtr) // 2 
    missingNums = arr[midPtr] - midPtr - 1

    return midPtr + k + 1

# Test cases
arr = [2,3,4,7,11]
k = 5
print(findKthPositive(arr, k))

arr = [1,2,3,4]
k = 2
print(findKthPositive(arr, k))
