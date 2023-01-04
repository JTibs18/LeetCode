# Given a palindromic string of lowercase English letters palindrome, replace exactly one character with any lowercase English letter so that the resulting string is not a palindrome and that it is the lexicographically smallest one possible.
# Return the resulting string. If there is no way to replace a character to make it not a palindrome, return an empty string.
# A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, a has a character strictly smaller than the corresponding character in b. For example, "abcc" is lexicographically smaller than "abcd" because the first position they differ is at the fourth character, and 'c' is smaller than 'd'.

import math

def breakPalindrome(palindrome): 
    ptr = 0
    lenPalindrome = len(palindrome)

    if lenPalindrome == 1: 
        return ""

    while ptr < lenPalindrome: 
        if palindrome[ptr] != "a" and ptr != math.floor(lenPalindrome / 2):
            return  palindrome[:ptr] + "a" + palindrome[ptr + 1:]
        elif ptr + 1 == lenPalindrome: 
            return palindrome[:ptr] + "b"
            
        ptr += 1 

# Test cases
palindrome = "abccba"
print(breakPalindrome(palindrome))

palindrome = "a"
print(breakPalindrome(palindrome))

palindrome = "aba"
print(breakPalindrome(palindrome))
