# You are given an array of strings words (0-indexed).
# In one operation, pick two distinct indices i and j, where words[i] is a non-empty string, and move any character from words[i] to any position in words[j].
# Return true if you can make every string in words equal using any number of operations, and false otherwise.

def makeEqual(words):
    letterCount = dict()

    for i in words:
        for letter in i:
            if letter not in letterCount:
                letterCount[letter] = 1
            else:
                letterCount[letter] += 1 
    
    for value in letterCount.values():
        if value % len(words) != 0:
            return False
    
    return True 

# Test cases
words = ["abc","aabc","bc"]
print(makeEqual(words))

words = ["ab","a"]
print(makeEqual(words))
