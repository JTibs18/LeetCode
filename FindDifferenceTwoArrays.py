# Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
# answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
# answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
# Note that the integers in the lists may be returned in any order.

from collections import Counter

def findDifference(nums1, nums2): 
    n1 = Counter(nums1)
    n2 = Counter(nums2)

    return [list(n1.keys() - n2.keys()), list(n2.keys() - n1.keys())]

# Test cases
nums1 = [1,2,3]
nums2 = [2,4,6]
print(findDifference(nums1, nums2))

nums1 = [1,2,3,3]
nums2 = [1,1,2,2]
print(findDifference(nums1, nums2))
