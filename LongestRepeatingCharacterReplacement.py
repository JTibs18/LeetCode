# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
# Return the length of the longest substring containing the same letter you can get after performing the above operations.

def characterReplacement(s, k): 
    characterCount = dict()
    ptr1 = 0 
    ptr2 = 0 
    maxSequence = 0 

    characterCount[s[ptr2]] = 1

    while ptr2 < len(s): 
        if (ptr2 - ptr1 + 1) - max(characterCount.values()) <= k:
            maxSequence = max(ptr2 - ptr1 + 1, maxSequence) 
            ptr2 += 1 
            if ptr2 < len(s): 
                if s[ptr2] in characterCount: 
                    characterCount[s[ptr2]] += 1
                else: 
                    characterCount[s[ptr2]] = 1
        else: 
            characterCount[s[ptr1]] -= 1 
            ptr1 += 1 
    
    return maxSequence

# Test cases
s = "ABAB"
k = 2
print(characterReplacement(s, k))

s = "AABABBA"
k = 1
print(characterReplacement(s, k))
