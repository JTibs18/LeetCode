# Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.
# Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.

def getCommon(nums1, nums2):
    ptr1 = 0
    ptr2 = 0 

    while ptr1 < len(nums1) and ptr2 < len(nums2):
        if nums1[ptr1] == nums2[ptr2]:
            return nums1[ptr1]
        elif nums1[ptr1] < nums2[ptr2]:
            ptr1 += 1
        else: 
            ptr2 += 1 
        
    return -1 

# Test cases
nums1 = [1,2,3]
nums2 = [2,4]
print(getCommon(nums1, nums2))

nums1 = [1,2,3,6]
nums2 = [2,3,4,5]
print(getCommon(nums1, nums2))
