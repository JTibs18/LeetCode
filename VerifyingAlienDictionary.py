# In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.
# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

def isAlienSorted(words, order): 
    orderCount = 0 
    alienDict = dict() 
    ptr1 = 0
    ptr2 = 1 

    for i in order: 
        alienDict[i] = orderCount
        orderCount += 1
    
    while ptr2 < len(words): 
        for indx, letter in enumerate(words[ptr1]): 
            if indx >= len(words[ptr2]) or alienDict[letter] > alienDict[words[ptr2][indx]]: 
                return False 
            elif alienDict[letter] < alienDict[words[ptr2][indx]]: 
                break

        ptr1 += 1 
        ptr2 += 1
    
    return True

# Test cases 
words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
print(isAlienSorted(words, order))

words = ["word","world","row"]
order = "worldabcefghijkmnpqstuvxyz"
print(isAlienSorted(words, order))

words = ["apple","app"]
order = "abcdefghijklmnopqrstuvwxyz"
print(isAlienSorted(words, order))
