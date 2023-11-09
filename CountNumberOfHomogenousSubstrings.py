# Given a string s, return the number of homogenous substrings of s. Since the answer may be too large, return it modulo 109 + 7.
# A string is homogenous if all the characters of the string are the same.
# A substring is a contiguous sequence of characters within a string.

def countHomogenous(s):
    ptr1 = 0 
    ptr2 = 1 
    count = 0 

    while ptr2 < len(s): 
        if s[ptr1] == s[ptr2]:
            ptr2 += 1 
        else:
            n = ptr2 - ptr1 
            count += (n * (n + 1)) // 2 
            ptr1 = ptr2 
            ptr2 = ptr1 + 1 
    
    n = ptr2 - ptr1 
    count += (n * (n + 1)) // 2 

    return count % ((10 ** 9) + 7)

# Test cases
s = 'abbcccaa'
print(countHomogenous(s))

s = 'xy'
print(countHomogenous(s))

s = 'zzzzz'
print(countHomogenous(s))
