# Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.
# A substring is a contiguous sequence of characters within a string.

def maxLengthBetweenEqualCharacters(s):
    maxLen = -1
    p1 = len(s) - 1

    while p1 >= 0:
        found = s.find(s[p1], 0, p1)
        if found != -1:
            tempLen = (p1 - found) - 1
            if  tempLen > maxLen:
                maxLen = tempLen
        p1 -= 1
    return maxLen

#Test Cases
s = "aa"
print(maxLengthBetweenEqualCharacters(s))

s = "abca"
print(maxLengthBetweenEqualCharacters(s))

s = "cbzxy"
print(maxLengthBetweenEqualCharacters(s))

s = "cbzcxy"
print(maxLengthBetweenEqualCharacters(s))

s = "bczcxy"
print(maxLengthBetweenEqualCharacters(s))

s = "cabbac"
print(maxLengthBetweenEqualCharacters(s))

s = "mgntdygtxrvxjnwksqhxuxtrv"
print(maxLengthBetweenEqualCharacters(s))
