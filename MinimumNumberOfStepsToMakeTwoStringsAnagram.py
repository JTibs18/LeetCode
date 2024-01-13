# You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.
# Return the minimum number of steps to make t an anagram of s.
# An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

# naive approach
def minSteps1(s, t):
    sDict = dict()
    tDict = dict()
    count = 0 

    for indx, val in enumerate(s):
        if val not in sDict:
            sDict[val] = 1
        else:
            sDict[val] += 1
        
        if t[indx] not in tDict:
            tDict[t[indx]] = 1
        else:
            tDict[t[indx]] += 1 

    for key, value in sDict.items():
        if key in tDict and value > tDict[key]:    
            count += value - tDict[key]
        elif key not in tDict:
            count += value

    return count
 
# faster runtime
def minSteps(s, t):
    sDict = dict()
    count = 0 

    for val in s:
        if val not in sDict:
            sDict[val] = 1
        else:
            sDict[val] += 1

    for key, value in sDict.items():
        if key in t and value > t.count(key):    
            count += value - t.count(key)
        elif key not in t:
            count += value

    return count

# Test cases
s = "bab"
t = "aba"
print(minSteps(s, t))

s = "leetcode"
t = "practice"
print(minSteps(s, t))

s = "anagram"
t = "mangaar"
print(minSteps(s, t))
