def countPrefixSuffixPairs(words):
    i = 0
    j = 1 
    count = 0

    def findLPS(w1):
        prevLPS, i = 0, 1 
        lps = [0] * len(w1)

        while i < len(w1):
            if w1[i] == w1[prevLPS]:
                lps[i] = prevLPS + 1
                prevLPS += 1 
                i += 1 
            elif prevLPS == 0:
                lps[i] = 0
                i += 1 
            else:
                prevLPS = lps[prevLPS - 1]

        return lps
    
    def isPrefixAndSuffix(w1, w2):
        if w1 in w2:
            return True 
        return False 

    while i < len(words) and j < len(words):
        lps = findLPS(words[j])
        
        if (max(lps) and isPrefixAndSuffix(words[i], words[j][:max(lps) + 1])) or words[i] == words[j]:
            count += 1 
        
        j += 1 

        if j == len(words):
            i += 1 
            j = i + 1 
        
    return count

# Test cases
words = ["a","aba","ababa","aa"]
print(countPrefixSuffixPairs(words))

words = ["pa","papa","ma","mama"]
print(countPrefixSuffixPairs(words))

words = ["abab","ab"]
print(countPrefixSuffixPairs(words))

words = ["b", "ba"]
print(countPrefixSuffixPairs(words))

words = ["a", "a"]
print(countPrefixSuffixPairs(words))

words = ["a","ccbb","cacbb"] # wrong testcase 