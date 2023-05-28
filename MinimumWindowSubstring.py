# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window.
# If there is no such substring, return the empty string "".
# The testcases will be generated such that the answer is unique.
# A substring is a contiguous sequence of characters within the string.
# with peusdocode help from: https://www.phind.com/search?cache=130e5142-e9b0-441f-b0f8-885396b52d3b

def minWindow(s, t): 
    charInT = dict()
    leftPtr = 0
    rightPtr = 0 
    windowCount = 0 
    minLength = len(s)
    result = ""

    for i in t: 
        if i in charInT: 
            charInT[i] += 1 
        else: 
            charInT[i] = 1 

    while rightPtr < len(s): 
        if s[rightPtr] in t: 
            charInT[s[rightPtr]] -= 1 
            if charInT[s[rightPtr]] >= 0: 
                windowCount += 1 
        
        rightPtr += 1 

        while windowCount == len(t):
            if rightPtr - leftPtr <= minLength: 
                minLength = rightPtr - leftPtr
                result = s[leftPtr : rightPtr]

            if s[leftPtr] in t: 
                charInT[s[leftPtr]] += 1 
                if charInT[s[leftPtr]] > 0: 
                    windowCount -= 1 

            leftPtr += 1 

    return result 

#Test cases
s = "ABC"
t = "B"
print(minWindow(s, t))

s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s, t))

s = "a"
t = "a"
print(minWindow(s, t))

s = "a"
t = "aa"
print(minWindow(s, t))
