# You have an array arr of length n where arr[i] = (2 * i) + 1 for all valid values of i (i.e., 0 <= i < n).
# In one operation, you can select two indices x and y where 0 <= x, y < n and subtract 1 from arr[x] and add 1 to arr[y] (i.e., perform arr[x] -=1 and arr[y] += 1). The goal is to make all the elements of the array equal. It is guaranteed that all the elements of the array can be made equal using some operations.
# Given an integer n, the length of the array, return the minimum number of operations needed to make all the elements of arr equal.

# naive solution
def minOperations1(n):
    arr = []
    value = 0
    operationCount = 0
    
    for i in range(n):
        arr.append((2 * i) + 1)

    if len(arr) % 2 == 0:
        value = (arr[len(arr) // 2] + arr[(len(arr) // 2) - 1]) // 2
    else:
        value = arr[len(arr) // 2]

    for i in range((len(arr) // 2), len(arr)):
        operationCount += arr[i] - value 

    return operationCount

# math equation, with help from https://leetcode.com/problems/minimum-operations-to-make-array-equal/solutions/1145020/js-python-java-c-easy-o-1-1-liner-mathematical-solutions-w-explanation/
# better solution because it is faster and takes less memory
def minOperations(n):
    return n * n // 4

# Test cases
n = 1
print(minOperations(n))

n = 2
print(minOperations(n))

n = 3
print(minOperations(n))

n = 4
print(minOperations(n))

n = 5
print(minOperations(n))

n = 6
print(minOperations(n))

n = 7
print(minOperations(n))

n = 8
print(minOperations(n))