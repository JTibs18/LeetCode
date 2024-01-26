# Given three integer arrays nums1, nums2, and nums3, return a distinct array containing all the values that are present in at least two out of the three arrays. You may return the values in any order.

def addToDict(arr, d):
    for i in set(arr):
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    return d
            
def twoOutOfThree(nums1, nums2, nums3):
    twoOfThree = []
    numCount = addToDict(nums1, dict())
    numCount = addToDict(nums2, numCount)
    numCount = addToDict(nums3, numCount)

    for key, val in numCount.items():
        if val >= 2: 
            twoOfThree.append(key)

    return twoOfThree

# Test cases
nums1 = [1,1,3,2]
nums2 = [2,3]
nums3 = [3]
print(twoOutOfThree(nums1, nums2, nums3))

nums1 = [3,1]
nums2 = [2,3]
nums3 = [1,2]
print(twoOutOfThree(nums1, nums2, nums3))

nums1 = [1,2,2]
nums2 = [4,3,3]
nums3 = [5]
print(twoOutOfThree(nums1, nums2, nums3))
