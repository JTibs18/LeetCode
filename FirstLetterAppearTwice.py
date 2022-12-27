# Given a string s consisting of lowercase English letters, return the first letter to appear twice.
# Note:
# A letter a appears twice before another letter b if the second occurrence of a is before the second occurrence of b.
# s will contain at least one letter that appears twice.

def repeatedCharacter(s): 
    letterCount = dict() 

    for i in s: 
        if i in letterCount: 
            letterCount[i] += 1 
        else: 
            letterCount[i] = 1 

        if letterCount[i] == 2: 
            return i
    
# Test cases 
s = "abccbaacz"
print(repeatedCharacter(s))

s = "abcdd"
print(repeatedCharacter(s))
