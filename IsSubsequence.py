# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

def isSubsequence(s, t):
    ptrS = 0

    if s == '': 
        return True

    for i in t:
        if s[ptrS] == i:
            ptrS += 1
        if ptrS >= len(s):
            return True

    return False

#Test Cases
s = 'abc'
t = 'ahbgdc'
print(isSubsequence(s, t))

s = "axc"
t = "ahbgdc"
print(isSubsequence(s, t))
