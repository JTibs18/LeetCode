# You are given an array of positive integers arr. Perform some operations (possibly none) on arr so that it satisfies these conditions:
# The value of the first element in arr must be 1.
# The absolute difference between any 2 adjacent elements must be less than or equal to 1. In other words, abs(arr[i] - arr[i - 1]) <= 1 for each i where 1 <= i < arr.length (0-indexed). abs(x) is the absolute value of x.
# There are 2 types of operations that you can perform any number of times:
# Decrease the value of any element of arr to a smaller positive integer.
# Rearrange the elements of arr to be in any order.
# Return the maximum possible value of an element in arr after performing the operations to satisfy the conditions.

def maximumElementAfterDecrementingAndRearranging(arr):
    arr.sort()
    prevNum = 0

    for i in arr:
        if i - prevNum <= 1: 
            prevNum = i
        else:
            prevNum += 1 

    return prevNum

# Test cases
arr = [2, 2, 1, 2, 1]
print(maximumElementAfterDecrementingAndRearranging(arr))

arr = [100, 1, 1000]
print(maximumElementAfterDecrementingAndRearranging(arr))

arr = [1, 2, 3, 4, 5]
print(maximumElementAfterDecrementingAndRearranging(arr))
