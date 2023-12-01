# Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average greater than or equal to threshold.

def numOfSubarrays(arr, k, threshold):
    ptr1 = 0
    ptr2 = k - 1
    numSubArrs = 0
    curSum = sum(arr[ptr1: ptr2])

    while ptr2 < len(arr) + 1:
        curSum += arr[ptr2]

        if curSum / k >= threshold:
            numSubArrs += 1 

        curSum -= arr[ptr1]
        ptr1 += 1
        ptr2 += 1

    return numSubArrs

# Test cases
arr = [2, 2, 2, 2, 5, 5, 5, 8]
k = 3
threshold = 4
print(numOfSubarrays(arr, k, threshold))

arr = [11, 13, 17, 23, 29, 31, 7, 5, 2, 3]
k = 3
threshold = 5
print(numOfSubarrays(arr, k, threshold))
