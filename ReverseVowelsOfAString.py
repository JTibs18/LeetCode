# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

# attempt 1: less memory, slower runtime 
def reverseVowels(s): 
    s = list(s)
    vowels = "aeiou"
    ptr1 = 0 
    ptr2 = len(s) - 1 

    while ptr1 < ptr2:
        if s[ptr1].lower() in vowels and s[ptr2].lower() in vowels: 
            temp = s[ptr1]
            s[ptr1] = s[ptr2]
            s[ptr2] = temp 
            ptr1 += 1
            ptr2 -=1 
        else: 
            if s[ptr1].lower() not in vowels: 
                ptr1 += 1 
            
            if s[ptr2].lower() not in vowels: 
                ptr2 -= 1 

    return "".join(s)

# attempt 2: more memory, faster runtime 
def reverseVowels2(s): 
    s = list(s)
    vowels = "aeiouAEIOU"
    ptr1 = 0 
    ptr2 = len(s) - 1 

    while ptr1 < ptr2:
        if s[ptr1] in vowels and s[ptr2] in vowels: 
            temp = s[ptr1]
            s[ptr1] = s[ptr2]
            s[ptr2] = temp 
            ptr1 += 1
            ptr2 -=1 
        else: 
            if s[ptr1] not in vowels: 
                ptr1 += 1 
            
            if s[ptr2] not in vowels: 
                ptr2 -= 1 
                
    return "".join(s)

# Test cases
s = "hello"
print(reverseVowels(s))

s = "leetcode"
print(reverseVowels(s))

s = "aA"
print(reverseVowels(s))
