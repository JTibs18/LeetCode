# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

def maxVowels(s, k): 
    numericS = []
    ptr1 = 0 
    ptr2 = k 
    vowelMax = 0 
    curCount = 0 

    for i in s: 
        if i in "aeiou": 
            numericS.append(1)
        else:
            numericS.append(0)

    curCount = sum(numericS[ptr1: ptr2])
    if (vowelMax < curCount): 
        vowelMax = curCount
    
    curCount -= numericS[ptr1]
    ptr1 += 1

    while ptr2 < len(numericS): 
        curCount += numericS[ptr2] 

        if curCount > vowelMax:
            vowelMax = curCount
        
        curCount -= numericS[ptr1]
        ptr1 += 1
        ptr2 += 1
        
    return vowelMax

# Test cases
s = "abciiidef" 
k = 3
print(maxVowels(s, k))

s = "aeiou"
k = 2
print(maxVowels(s, k))

s = "leetcode" 
k = 3
print(maxVowels(s, k))

s = "weallloveyou"
k = 7 
print(maxVowels(s, k))
