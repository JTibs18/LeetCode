# Given a string s of '(' , ')' and lowercase English characters.
# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.
# Formally, a parentheses string is valid if and only if:
#   It is the empty string, contains only lowercase characters, or
#   It can be written as AB (A concatenated with B), where A and B are valid strings, or
#   It can be written as (A), where A is a valid string.

def minRemoveToMakeValid(s):
    stack = []
    newS = ''

    for i in s:
        if i == "(":
            stack.append(i)
            newS += i
        elif i == ")" and stack:
            stack.pop()
            newS += i
        elif i != ")" and i != "(":
            newS += i
            
    for i in range(len(newS) - 1, -1, -1):
        if not stack:
            break
        
        if newS[i] == "(":
            newS = newS[:i] + newS[i + 1:]
            stack.pop()

    return newS

# Test cases
s = "lee(t(c)o)de)"
print(minRemoveToMakeValid(s))

s = "a)b(c)d"
print(minRemoveToMakeValid(s))

s = "))(("
print(minRemoveToMakeValid(s))

s = "(a(b(c)d)"
print(minRemoveToMakeValid(s))
