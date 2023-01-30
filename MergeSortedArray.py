# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

def merge(nums1, m, nums2, n): 
    count = m + n 
    ptr1 = 0 
    ptr2 = 0 

    while count and len(nums2) > 0 and len(nums2) > ptr2: 
        if nums1[ptr1] > nums2[ptr2] or count <= n: 
            nums1[ptr1:ptr1] = [nums2[ptr2]]
            nums1.pop()
            ptr1 += 1
            ptr2 += 1 
            n -= 1
        else: 
            ptr1 += 1 
           
        count -= 1
    print(nums1)

# Test cases 
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
merge(nums1, m, nums2, n)

nums1 = [1]
m = 1
nums2 = []
n = 0
merge(nums1, m, nums2, n)

nums1 = [0]
m = 0
nums2 = [1]
n = 1
merge(nums1, m, nums2, n)

nums1 = [2, 0]
m = 1
num2 = [1]
n = 1
merge(nums1, m, nums2, n)

nums1 = [-1,0,0,3,3,3,0,0,0]
m = 6
nums2 = [1, 2, 2]
n = 3
merge(nums1, m, nums2, n)

nums1 = [4, 0, 0, 0, 0, 0]
m = 1
nums2 = [1, 2, 3, 4, 5]
n = 5
merge(nums1, m, nums2, n)