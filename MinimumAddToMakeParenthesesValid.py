# A parentheses string is valid if and only if:
#   It is the empty string,
#   It can be written as AB (A concatenated with B), where A and B are valid strings, or
#   It can be written as (A), where A is a valid string.
# You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.
#   For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
# Return the minimum number of moves required to make s valid.

# stack, faster runtime but more memory
def minAddToMakeValid1(s):
    bracketStack = []
    moveCount = 0 

    for i in s:
        if i == "(":
            bracketStack.append(i)
        elif bracketStack:
            bracketStack.pop()
        else:
            moveCount += 1 
    
    return moveCount + len(bracketStack)

# greedy, slower runtime but less memory
def minAddToMakeValid(s):
    openBracketCount = 0
    moveCount = 0 

    for val in s:
        if val == "(":
            openBracketCount += 1 
        elif openBracketCount > 0:  
            openBracketCount -= 1
        else: 
            moveCount += 1 
    
    return openBracketCount + moveCount

# Test cases
s = "())"
print(minAddToMakeValid(s))

s = "((("
print(minAddToMakeValid(s))

s = ")()"
print(minAddToMakeValid(s))

s = "()))(("
print(minAddToMakeValid(s))
