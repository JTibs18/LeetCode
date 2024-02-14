# You are given a 0-indexed string s and a dictionary of words dictionary. You have to break s into one or more non-overlapping substrings such that each substring is present in dictionary. There may be some extra characters in s which are not present in any of the substrings.
# Return the minimum number of extra characters left over if you break up s optimally.

def minExtraChar(s, dictionary):
    def helper(s, dictionary, memo={}):
        if s in memo:
            return memo[s]
        
        if s == "":
            return 0
        
        removedLetters = float("inf")

        for word in dictionary:
            if word in s and s.index(word) == 0:
                removedLetters = min(removedLetters, helper(s[len(word):], dictionary, memo))

        removedLetters = min(removedLetters, helper(s[1:], dictionary, memo) + 1)

        memo[s] = removedLetters
        return memo[s]
    
    return helper(s, dictionary)

# Test cases
s = "leetscode"
dictionary = ["leet","code","leetcode"]
print(minExtraChar(s, dictionary))

s = "sayhelloworld"
dictionary = ["hello","world"]
print(minExtraChar(s, dictionary))

s = "ecolloycollotkvzqpdaumuqgs"
dictionary = ["flbri","uaaz","numy","laper","ioqyt","tkvz","ndjb","gmg","gdpbo","x","collo","vuh","qhozp","iwk","paqgn","m","mhx","jgren","qqshd","qr","qpdau","oeeuq","c","qkot","uxqvx","lhgid","vchsk","drqx","keaua","yaru","mla","shz","lby","vdxlv","xyai","lxtgl","inz","brhi","iukt","f","lbjou","vb","sz","ilkra","izwk","muqgs","gom","je"]
print(minExtraChar(s, dictionary))

s = "metzeaencgpgvsckjrqafkxgyzbe"
dictionary = ["zdzz","lgrhy","r","ohk","zkowk","g","zqpn","anoni","ka","qafkx","t","jr","xdye","mppc","bqqb","encgp","yf","vl","ctsxk","gn","cujh","ce","rwrpq","tze","zxhg","yzbe","c","o","hnk","gv","uzbc","xn","kk","ujjd","vv","mxhmv","ugn","at","kumr","ensv","x","uy","gb","ae","jljuo","xqkgj"]
print(minExtraChar(s, dictionary)) 
