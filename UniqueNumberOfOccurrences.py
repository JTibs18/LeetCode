# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

def uniqueOccurrences(arr):
    occurrences = dict()

    for i in arr:
        if i not in occurrences:
            occurrences[i] = 1 
        else:
            occurrences[i] += 1 

    if len(set(occurrences.values())) == len(occurrences):
        return True
    return False

# Test cases
arr = [1,2,2,1,1,3]
print(uniqueOccurrences(arr))

arr = [1, 2]
print(uniqueOccurrences(arr))

arr = [-3,0,1,-3,1,1,1,-3,10,0]
print(uniqueOccurrences(arr))
