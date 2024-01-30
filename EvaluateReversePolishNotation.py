# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
# Evaluate the expression. Return an integer that represents the value of the expression.
# Note that:
#   The valid operators are '+', '-', '*', and '/'.
#   Each operand may be an integer or another expression.
#   The division between two integers always truncates toward zero.
#   There will not be any division by zero.
#   The input represents a valid arithmetic expression in a reverse polish notation.
#   The answer and all the intermediate calculations can be represented in a 32-bit integer.

import math

def evalPRN(tokens):
    stack = []

    for i in tokens:
        if not i[-1].isnumeric():
            if i == "+":
                stack.append(stack.pop() + stack.pop())
            elif i == "-":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 - num1)
            elif i == "*":
                stack.append(stack.pop() * stack.pop())
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                if num1 * num2 > 0:
                    stack.append(num2 // num1)
                else: 
                    stack.append(math.ceil(num2 / num1))
        else:
            if i[0] == "-":
                stack.append(-1 * int(i[1:]))
            else:
                stack.append(int(i))

    return stack.pop()

# Test cases
tokens = ["2", "1", "+", "3", "*"]
print(evalPRN(tokens))

tokens = ["4", "13", "5", "/", "+"]
print(evalPRN(tokens))

tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(evalPRN(tokens))

tokens = ["4", "3", "-"]
print(evalPRN(tokens))
