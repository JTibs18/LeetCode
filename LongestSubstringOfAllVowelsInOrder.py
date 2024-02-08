# A string is considered beautiful if it satisfies the following conditions:
#   Each of the 5 English vowels ('a', 'e', 'i', 'o', 'u') must appear at least once in it.
#   The letters must be sorted in alphabetical order (i.e. all 'a's before 'e's, all 'e's before 'i's, etc.).
# For example, strings "aeiou" and "aaaaaaeiiiioou" are considered beautiful, but "uaeio", "aeoiu", and "aaaeeeooo" are not beautiful.
# Given a string word consisting of English vowels, return the length of the longest beautiful substring of word. If no such substring exists, return 0.
# A substring is a contiguous sequence of characters in a string.

def longestBeautifulSubstring(word):
    vowels = ["a", "e", "i", "o", "u"]
    ptr1 = 0
    ptr2 = 0
    vPtr1 = 0
    vPtr2 = 0
    longestSubstring = 0 

    while ptr2 < len(word):
        if vowels[vPtr1] == word[ptr2]:
            ptr2 += 1 

            if vPtr1 == vPtr2 and vPtr2 < len(vowels) - 1:
                vPtr2 += 1 
        elif vowels[vPtr2] == word[ptr2]:
            ptr2 += 1 
            vPtr1 = vPtr2

            if vPtr2 < len(vowels) - 1:
                vPtr2 += 1
        else:
            if vPtr2 == len(vowels) - 1 and vPtr1 == vPtr2:
                longestSubstring = max(longestSubstring, ptr2 - ptr1)

            if ptr1 == ptr2:
                ptr2 += 1
                
            ptr1 = ptr2 
            vPtr1 = 0 
            vPtr2 = 0

    if vPtr2 == len(vowels) - 1 and vPtr1 == vPtr2:
        longestSubstring = max(longestSubstring, ptr2 - ptr1)

    return longestSubstring

# Test cases
word = "aeiaaioaaaaeiiiiouuuooaauuaeiu"
print(longestBeautifulSubstring(word))

word = "aeeeiiiioooauuuaeiou"
print(longestBeautifulSubstring(word))

word = "a"
print(longestBeautifulSubstring(word))
