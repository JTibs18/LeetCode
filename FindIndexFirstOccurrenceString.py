# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

def strStr(haystack, needle): 
    ptr1 = 0 
    ptr2 = len(needle)

    while ptr2 <= len(haystack):
        if needle == haystack[ptr1: ptr2]: 
            return ptr1
        else: 
            ptr1 += 1
            ptr2 += 1

    return -1

# Test cases 
haystack = "sadbutsad"
needle = "sad"
print(strStr(haystack, needle))

haystack = "leetcode"
needle = "leeto"
print(strStr(haystack, needle))

haystack = "a"
needle = "a"
print(strStr(haystack, needle))