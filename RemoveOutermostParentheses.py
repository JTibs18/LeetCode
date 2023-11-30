# A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.
# For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
# A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.
# Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.
# Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.

# stack, slower runtime 
def removeOuterParentheses1(s):
    stack = []
    outputString = ''

    for i in s: 
        if stack and i == "(":
            outputString += i 
            stack.append(i)
        elif len(stack) > 1 and i == ")":
            stack.pop()
            outputString += i 
        elif not stack: 
            stack.append(i)
        else: 
            stack.pop()

    return outputString

# counting brackets, faster runtime 
def removeOuterParentheses(s):
    bracketCount = 0 
    outputString = ''

    for i in s: 
        if (bracketCount and i == "(") or (bracketCount > 1 and i == ")"):  
            outputString += i 
       
        if i == "(":
            bracketCount += 1
        else: 
            bracketCount -= 1 
    
    return outputString

# Test cases
s = "(()())(())"
print(removeOuterParentheses(s))

s = "(()())(())(()(()))"
print(removeOuterParentheses(s))

s = "()()"
print(removeOuterParentheses(s))
