# Given a string s, return the number of unique palindromes of length three that are a subsequence of s.
# Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.
# A palindrome is a string that reads the same forwards and backwards.
# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
# For example, "ace" is a subsequence of "abcde".

def countPalindromicSubsequence(s):
    letterCount = dict()
    palindromeCount = 0 

    for indx, val in enumerate(s): 
        if val in letterCount:
            letterCount[val].append(indx)
        else: 
            letterCount[val] = [indx]

    for values in letterCount.values():
        if len(values) > 1: 
            palindromeCount += len(set(s[values[0] + 1:values[-1]]))
                
    return palindromeCount

# Test cases
s = "aabca"
print(countPalindromicSubsequence(s))

s = 'adc'
print(countPalindromicSubsequence(s))

s = "bbcbaba"
print(countPalindromicSubsequence(s))

s = "tlpjzdmtwderpkpmgoyrcxttiheassztncqvnfjeyxxp"
print(countPalindromicSubsequence(s))
