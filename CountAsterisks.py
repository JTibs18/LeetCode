# You are given a string s, where every two consecutive vertical bars '|' are grouped into a pair. In other words, the 1st and 2nd '|' make a pair, the 3rd and 4th '|' make a pair, and so forth.
# Return the number of '*' in s, excluding the '*' between each pair of '|'.
# Note that each '|' will belong to exactly one pair.

# runs faster, same memory
def countAsterisks1(s):  
    inPair = False 
    asterisksCount = 0 

    for i in s: 
        if i == "|":
            inPair = not inPair
        elif i == "*" and not inPair:
            asterisksCount += 1 
    
    return asterisksCount

# runs slower, same memory
def countAsterisks(s):
    return sum(char.count('*') for char in s.split('|')[0::2])

# Test cases
s = "l|*e*et|c**o|*de|"
print(countAsterisks(s))

s = "iamprogrammer"
print(countAsterisks(s))

s = "yo|uar|e**|b|e***au|tifu|l"
print(countAsterisks(s))
