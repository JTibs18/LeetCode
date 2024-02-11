# You are given a 0-indexed string array words having length n and containing 0-indexed strings.
# You are allowed to perform the following operation any number of times (including zero):
# Choose integers i, j, x, and y such that 0 <= i, j < n, 0 <= x < words[i].length, 0 <= y < words[j].length, and swap the characters words[i][x] and words[j][y].
# Return an integer denoting the maximum number of palindromes words can contain, after performing some operations.
# Note: i and j may be equal during an operation.

def maxPalindromesAfterOperations(words):
    letters = dict()
    odds = 0
    evens = 0 
    wordCount = 0 

    for i in words:
        for c in i:
            if c not in letters:
                letters[c] = 1
            else:
                letters[c] += 1 

    for val in letters.values():
        if val % 2 == 1:
            odds += 1
            evens += val - 1 
        else:
            evens += val 
    
    words = sorted(words, key=len)

    for i in words:
        if len(i) % 2 != 0 and odds - 1 >= 0 and evens - len(i) + 1 >= 0:
            odds -= 1 
            evens -= len(i) - 1
            wordCount += 1 
        elif evens - len(i) >= 0:
            evens -= len(i)
            wordCount += 1
            
    return wordCount

# Test cases
words = ["abbb","ba","aa"]
print(maxPalindromesAfterOperations(words))

words = ["abc","ab"]
print(maxPalindromesAfterOperations(words))

words = ["cd","ef","a"]
print(maxPalindromesAfterOperations(words))

words = ["a","ccc"]
print(maxPalindromesAfterOperations(words))

words = ["a","a","caa"]
print(maxPalindromesAfterOperations(words))

words = ["aagha","bc"]
print(maxPalindromesAfterOperations(words))

words = ["bb","dfbf","habb"]
print(maxPalindromesAfterOperations(words))

words = ["rqfsx","kja","mx","r"]
print(maxPalindromesAfterOperations(words))
