# You are given a string s consisting of lowercase English letters, and you are allowed to perform operations on it. In one operation, you can replace a character in s with another lowercase English letter.
# Your task is to make s a palindrome with the minimum number of operations possible. If there are multiple palindromes that can be made using the minimum number of operations, make the lexicographically smallest one.
# A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, string a has a letter that appears earlier in the alphabet than the corresponding letter in b.
# Return the resulting palindrome string.

# faster runtime but takes up more memory 
def makeSmallestPalindrome1(s): 
    ptr1 = 0 
    ptr2 = len(s) - 1
    s = list(s)

    while ptr1 < ptr2:
        if s[ptr1] != s[ptr2]:
            if s[ptr1] < s[ptr2]: 
                s[ptr2] = s[ptr1]
            else: 
                s[ptr1] = s[ptr2]

        ptr1 += 1
        ptr2 -= 1

    return ''.join(s)

# slower runtime but takes up less memory
def makeSmallestPalindrome(s): 
    ptr1 = 0 
    ptr2 = len(s) - 1
    palindrome = ''

    while ptr1 < ptr2:
        palindrome += min(s[ptr1], s[ptr2])

        ptr1 += 1
        ptr2 -= 1
    
    reversePalindrome = palindrome[::-1]
    
    if ptr1 == ptr2: 
        palindrome += s[ptr1]

    palindrome += reversePalindrome  

    return palindrome

# Test cases
s = "egcfe"
print(makeSmallestPalindrome(s))

s = "abcd"
print(makeSmallestPalindrome(s))

s = "seven"
print(makeSmallestPalindrome(s))
