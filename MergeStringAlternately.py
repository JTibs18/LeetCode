# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
# Return the merged string.

def mergeAlternatively(word1, word2): 
    indx = 0
    merged = ''

    while (indx < len(word1) and indx < len(word2)):
        merged += word1[indx] + word2[indx]
        indx += 1 

    if indx < len(word1): 
        merged += word1[indx:]
    
    if indx < len(word2): 
        merged += word2[indx:]

    return merged 

# Test cases
word1 = "abc"
word2 = "pqr"
print(mergeAlternatively(word1, word2))

word1 = "ab"
word2 = "pqrs"
print(mergeAlternatively(word1, word2))

word1 = "abcd"
word2 = "pq"
print(mergeAlternatively(word1, word2))