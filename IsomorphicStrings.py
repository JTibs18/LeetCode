# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

def isIsomorphic(s, t):
    mapping = dict()

    for indx, val in enumerate(s): 
        if val in mapping: 
            if mapping[val] != t[indx]:
                return False 
        elif t[indx] not in mapping.values(): 
            mapping[val] = t[indx]
        else: 
            return False
    return True  

# Test cases
s = "egg"
t = "add"
print(isIsomorphic(s, t))

s = "foo"
t = "bar"
print(isIsomorphic(s, t))

s = "paper"
t = "title"
print(isIsomorphic(s, t))

s = "badc"
t = "baba"
print(isIsomorphic(s, t))
