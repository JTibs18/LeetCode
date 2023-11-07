# Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.

# slower solution 
def longestValidParentheses1(s): 
    validParentheses = [0 for _ in range(len(s))]
    openBrackets = []
    validParenthesesCount = 0 
    count = 0 

    for indx, val in enumerate(s):
        if val == '(': 
            openBrackets.append(indx)
        else:
            if len(openBrackets) > 0:
                openBracketIndex = openBrackets.pop()
                validParentheses[openBracketIndex] = 1
                validParentheses[indx] = 1

    for i in validParentheses:
        if i == 1: 
            count += 1 
        else: 
            validParenthesesCount = max(count, validParenthesesCount)
            count = 0 

    return max(count, validParenthesesCount)

# faster solution
def longestValidParentheses(s):
    stack = [-1]
    maxLength = 0 

    for indx, val in enumerate(s):
        if val == "(":
            stack.append(indx)
        else: 
            if stack:
                stack.pop()

                if stack: 
                    maxLength = max(maxLength, indx - stack[-1])
                else:
                    stack.append(indx)
    
    return maxLength

# Test cases
s = "(()"
print(longestValidParentheses(s))

s = ")()())"
print(longestValidParentheses(s))

s = ""
print(longestValidParentheses(s))

s = "((()((((())()"
print(longestValidParentheses(s))
