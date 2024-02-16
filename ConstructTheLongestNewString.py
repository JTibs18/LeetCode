# You are given three integers x, y, and z.
# You have x strings equal to "AA", y strings equal to "BB", and z strings equal to "AB". You want to choose some (possibly all or none) of these strings and concatenate them in some order to form a new string. This new string must not contain "AAA" or "BBB" as a substring.
# Return the maximum possible length of the new string.
# A substring is a contiguous non-empty sequence of characters within a string.

# naive solution
def longestString1(x, y, z):
    newStringLen = 0

    if x <= y + 1:
        newStringLen += x * 2
    else:
        newStringLen += (y + 1) * 2

    if y <= x:
        newStringLen += y * 2
    else:
        newStringLen += (x + 1) * 2
    
    newStringLen += z * 2 

    return newStringLen

# more clever solution: faster runtime
def longestString(x, y, z):
    newStringLen = z * 2 

    if x < y:
        newStringLen += (x * 4) + 2
    elif x > y:
        newStringLen += (y * 4) + 2
    else:
        newStringLen += x * 4

    return newStringLen

# Test cases
x = 2
y = 5
z = 1
print(longestString(x, y, z))

x = 3
y = 2
z = 2
print(longestString(x, y, z))

x = 1 
y = 39
z = 14
print(longestString(x, y, z))
