# Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. That is, no letter appears in a single substring more than once.
# Return the minimum number of substrings in such a partition.
# Note that each character should belong to exactly one substring in a partition.

def partitionString(s): 
    count = 0 
    substring = set() 

    for i in s: 
        if i in substring: 
            count += 1 
            substring = set()
        substring.add(i)
    
    return count + 1 

# Test cases
s = "abacaba"
print(partitionString(s))

s = "ssssss"
print(partitionString(s))

s = "hdklqkcssgxlvehva"
print(partitionString(s))
