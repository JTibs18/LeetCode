# Given a string s, find the length of the longest substring without repeating characters.
# GREAT SOLUTION! Top 89% time and top 85% space efficient 

def lengthOfLongestSubstring(s):
    maxC = 0
    uniqueL = set()

    if len(s) == 0:
        return 0
    elif len(s) == 1:
        return 1

    p1 = 0

    for char in s:
        if char in uniqueL:
            if len(uniqueL) > maxC:
                maxC = len(uniqueL)
            while s[p1] != char:
                uniqueL.remove(s[p1])
                p1 += 1
            p1 += 1
            uniqueL.add(char)
        else:
            uniqueL.add(char)
    if len(uniqueL) > maxC:
        maxC = len(uniqueL)
    return maxC

#Test Cases
s = "abcabcbb"
print(lengthOfLongestSubstring(s))

s = "bbbbb"
print(lengthOfLongestSubstring(s))

s = "pwwkew"
print(lengthOfLongestSubstring(s))

s = ""
print(lengthOfLongestSubstring(s))

s = " "
print(lengthOfLongestSubstring(s))

s = "au"
print(lengthOfLongestSubstring(s))

s = "dvdf"
print(lengthOfLongestSubstring(s))
