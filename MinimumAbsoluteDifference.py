# Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.
# Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows
#   a, b are from arr
#   a < b
#   b - a equals to the minimum absolute difference of any two elements in arr

def minimumAbsDifference(arr):
    diff = dict()
    arr.sort()

    for i in range(len(arr) - 1):
        curDiff = arr[i + 1] - arr[i]

        if curDiff in diff:
            diff[curDiff].append([arr[i], arr[i + 1]])
        else:
            diff[curDiff] = [[arr[i], arr[i + 1]]]    

    return diff[min(diff.keys())]

# Test cases
arr = [4,2,1,3]   
print(minimumAbsDifference(arr))

arr = [1,3,6,10,15]
print(minimumAbsDifference(arr))

arr = [3,8,-10,23,19,-4,-14,27]
print(minimumAbsDifference(arr))
