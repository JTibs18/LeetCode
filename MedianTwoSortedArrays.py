# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

def findKedianSortedArrays(nums1, nums2):
    nums1.extend(nums2)
    nums1.sort()
    size = len(nums1)
    if size % 2 == 0:
        indx1 = (size // 2) - 1
        indx2 = indx1 + 1
        return ((nums1[indx1] + nums1[indx2]) / 2)
    else:
        indx = size // 2
        return nums1[indx]

#Test Cases
nums1 = [1, 3]
nums2 = [2]
print(findKedianSortedArrays(nums1, nums2))

nums1 = [1, 2]
nums2 = [3, 4]
print(findKedianSortedArrays(nums1, nums2))

nums1 = [0, 0]
nums2 = [0, 0]
print(findKedianSortedArrays(nums1, nums2))

nums1 = []
nums2 = [1]
print(findKedianSortedArrays(nums1, nums2))

nums1 = [2]
nums2 = []
print(findKedianSortedArrays(nums1, nums2))
