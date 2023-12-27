# Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.
# After doing so, return the array.

def replaceElements(arr):
    returnArr = [-1]
    curMax = -1

    for i in range(len(arr) - 1, 0, -1):
        if arr[i] > curMax:
            curMax = arr[i]

        returnArr.append(curMax)

    return returnArr[::-1]

# Test cases
arr = [17,18,5,4,6,1]
print(replaceElements(arr))

arr = [400]
print(replaceElements(arr))