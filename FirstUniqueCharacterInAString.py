# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

def firstUniqChar(s): 
    letterCount = dict() 

    for i in s: 
        if i in letterCount: 
            letterCount[i] += 1 
        else: 
            letterCount[i] = 1 
    
    for indx, val in enumerate(s): 
        if letterCount[val] == 1: 
            return indx
    
    return -1 

# Test cases 
s = "leetcode"
print(firstUniqChar(s))

s = "loveleetcode"
print(firstUniqChar(s))

s = "aabb"
print(firstUniqChar(s))

s = "dddccdbba"
print(firstUniqChar(s))