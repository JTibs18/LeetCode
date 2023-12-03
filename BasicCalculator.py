# Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.
# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

def doMath(stack):
    total = int(stack[0])

    for i in range(1, len(stack), 2): 
        if stack[i] == "+":
            total += int(stack[i + 1])
        else: 
            total -= int(stack[i + 1])
    
    return total

def consolidateNums(stack):
    curNum = ''
    newStack = []

    for i in stack: 
        if i == "+" or i == "-":
            if curNum == '':
                curNum = "0"
                
            newStack.append(curNum)
            newStack.append(i)
            curNum = ''
        else:
            curNum += str(i)

    if curNum == '':
        curNum = "0"

    newStack.append(curNum)
    return newStack    

def calculate(s):
    stack = []
    s = s.replace(" ", '')

    for i in s: 
        if i == ")":
            curStack = []

            while stack and stack[-1] != "(":
                curStack.append(stack.pop())                
            
            stack.pop()
            stack.append(doMath(consolidateNums(curStack[::-1])))
        else:
            stack.append(i)
    
    return doMath(consolidateNums(stack))

# Test cases
s = "1 + 1"
print(calculate(s))

s = " 2-1 + 2 "
print(calculate(s))

s = "(1+(4+5+2)-3)+(6+8)"
print(calculate(s))

s = "2147483647"
print(calculate(s))

s = "1-(     -2)"
print(calculate(s))
