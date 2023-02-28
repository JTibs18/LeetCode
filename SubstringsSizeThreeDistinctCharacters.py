# A string is good if there are no repeated characters.
# Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.
# Note that if there are multiple occurrences of the same substring, every occurrence should be counted.
# A substring is a contiguous sequence of characters in a string.

def countGoodSubstrings(s): 
    ptr1 = 0 
    count = 0 

    while ptr1 + 2 < len(s): 
        if s[ptr1] != s[ptr1 + 1] and s[ptr1 + 1] != s[ptr1 + 2] and s[ptr1 + 2] != s[ptr1]: 
            count += 1 

        ptr1 += 1 
    
    return count

# Test cases 
s = "xyzzaz"
print(countGoodSubstrings(s))

s = "aababcabc"
print(countGoodSubstrings(s))
