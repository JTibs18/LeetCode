# You are given a string s, which contains stars *.
# In one operation, you can:
# Choose a star in s.
# Remove the closest non-star character to its left, as well as remove the star itself.
# Return the string after all stars have been removed.
# Note:
# The input will be generated such that the operation is always possible.
# It can be shown that the resulting string will always be unique.

# runs faster, takes more memory
def removeStars1(s): 
    letterStack = []
    remainingLetters = ""

    for i in s: 
        if i == "*":
            letterStack.pop()
        else: 
            letterStack.append(i)

    for i in letterStack:
        remainingLetters += i
    
    return remainingLetters

# less memory, runs slower 
def removeStars(s): 
    letterStack = ""

    for i in s: 
        if i == "*":
            letterStack = letterStack[:-1]
        else: 
            letterStack +=  i
    
    return letterStack

# Test cases
s = "leet**cod*e"
print(removeStars(s))

s = "erase*****"
print(removeStars(s))
