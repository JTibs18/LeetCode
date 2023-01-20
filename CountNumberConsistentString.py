# You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.
# Return the number of consistent strings in the array words.
from collections import Counter
# slowest solution, takes up more space
def countConsistentStrings1(allowed, words):
    consistentStrings = 0
    validString = True 

    for i in words: 
        counter = Counter(i)
        validString = True 
        for letter in counter.keys(): 
            if letter not in allowed: 
                validString = False
                break   
        if validString == True: 
            consistentStrings += 1 
    
    return consistentStrings

# Faster than #1 
def countConsistentStrings2(allowed, words):
    consistentStrings = 0
    validString = True 

    for i in words: 
        counter = set(i)
        validString = True 
        for letter in counter: 
            if letter not in allowed: 
                validString = False
                break   
        if validString == True: 
            consistentStrings += 1 
    
    return consistentStrings
        
# Slightly faster solution than #2 
def countConsistentStrings(allowed, words):
    consistentStrings = 0
    validString = True 

    for i in words: 
        counter = set(i)
        validString = True 
        if len(counter) <= len(allowed): 
            for letter in counter: 
                if letter not in allowed: 
                    validString = False
                    break   
            if validString == True: 
                consistentStrings += 1 
    
    return consistentStrings

# Test cases 
allowed = "ab"
words =  ["ad","bd","aaab","baa","badab"]
print(countConsistentStrings(allowed, words))

allowed = "abc"
words = ["a","b","c","ab","ac","bc","abc"]
print(countConsistentStrings(allowed, words))

allowed = "cad"
words = ["cc","acd","b","ba","bac","bad","ac","d"]
print(countConsistentStrings(allowed, words))
