# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

def isValid(s):
    stack = []
    for value in s:
        if len(stack) == 0:
            stack.append(value)
        elif value == ")":
            if stack.pop() != "(":
                return False
        elif value == "]":
             if stack.pop() != "[":
                 return False
        elif value == "}":
            if stack.pop() != "{":
                return False
        else:
            stack.append(value)
    if len(stack) > 0:
        return False
    else:
        return True

#Test cases
s = "()"
print(isValid(s))

s = "()[]{}"
print(isValid(s))

s = "(]"
print(isValid(s))

s = "([)]"
print(isValid(s))

s = "{[]}"
print(isValid(s))
