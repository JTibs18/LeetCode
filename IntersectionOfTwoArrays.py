# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

def intersection(nums1, nums2):
    intersect = []
    nums2 = set(nums2)

    for i in set(nums1):
        if i in set(nums2):
            intersect.append(i)

    return intersect

# Test cases
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersection(nums1, nums2))

nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(intersection(nums1, nums2))
