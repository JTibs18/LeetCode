# For weekly contest #324 Question #1
 
# You are given a 0-indexed string array words.
# Two strings are similar if they consist of the same characters.
# For example, "abca" and "cba" are similar since both consist of characters 'a', 'b', and 'c'.
# However, "abacba" and "bcfd" are not similar since they do not consist of the same characters.
# Return the number of pairs (i, j) such that 0 <= i < j <= word.length - 1 and the two strings words[i] and words[j] are similar.

def similarPairs(words): 
    indx1 = 0
    indx2 = 1 
    pairs = 0

    while indx1 < len(words) - 1: 
        if set(words[indx1]) == set(words[indx2]): 
            pairs += 1
        if indx2 + 1 > len(words) - 1: 
            indx1 += 1 
            indx2 = indx1 + 1 
        else: 
            indx2 += 1

    return pairs

# Test cases 
words = ["aba","aabb","abcd","bac","aabc"]
print(similarPairs(words))

words = ["aabb","ab","ba"]
print(similarPairs(words))

words = ["nba","cba","dba"]
print(similarPairs(words))