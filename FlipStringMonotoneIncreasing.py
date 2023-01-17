# A binary string is monotone increasing if it consists of some number of 0's (possibly none), followed by some number of 1's (also possibly none).
# You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.
# Return the minimum number of flips to make s monotone increasing.

from collections import Counter

# First attempt, slower algorithm that uses more memory 
def minFlipsMonoIncr1(s): 
    flips = []
    smallest = len(s)
    zeroCount = Counter(s)["0"]
    oneCount = 0

    for val in s:
        if val == "0": 
            zeroCount -= 1 

        flips.append(zeroCount + oneCount)
        
        if val == "1": 
            oneCount += 1 
    
    smallest = min(flips)
    
    if smallest == len(s): 
        return 0
    return smallest

# Faster algorithm that uses less memory 
def minFlipsMonoIncr(s): 
    smallest = len(s)
    zeroCount = Counter(s)["0"]
    oneCount = 0

    for val in s:
        if val == "0": 
            zeroCount -= 1 
        if zeroCount + oneCount < smallest: 
            smallest = zeroCount + oneCount
        if val == "1": 
            oneCount += 1 
    
    if smallest == len(s): 
        return 0
    return smallest

# Test cases
s = "00110"
print(minFlipsMonoIncr(s))

s = "010110"
print(minFlipsMonoIncr(s))

s = "00011000"
print(minFlipsMonoIncr(s))

s = "11111"
print(minFlipsMonoIncr(s))

s = "0101100011"
print(minFlipsMonoIncr(s))
