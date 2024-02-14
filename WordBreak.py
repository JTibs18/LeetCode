# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.

def wordBreak(s, wordDict):
    def helper(s, wordDict, memo={}):
        if s in memo:
            return memo[s]
        
        if s == "":
            return True 

        for word in wordDict:
            if word in s and s.index(word) == 0:
                if helper(s[len(word):], wordDict, memo):
                    memo[s] = True 
                    return memo[s] 
        
        memo[s] = False
        return memo[s]

    return helper(s, wordDict)

# Test cases
s = "leetcode"
wordDict = ["leet", "code"]
print(wordBreak(s, wordDict))

s = "applepenapple"
wordDict = ["apple","pen"]
print(wordBreak(s, wordDict))

s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
print(wordBreak(s, wordDict))
