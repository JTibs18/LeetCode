# Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

def repeatedSubstringPattern(s):
    lengthSequence = len(s)

    for i in range(1, lengthSequence // 2 + 1):
        if lengthSequence % i == 0 and s[:i] * (lengthSequence // len(s[:i])) == s:
            return True 
        
    return False

# Test cases
s = "abab"
print(repeatedSubstringPattern(s))

s = 'aba'
print(repeatedSubstringPattern(s))

s = 'abcabcabcabc'
print(repeatedSubstringPattern(s))
