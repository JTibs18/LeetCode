# A boolean expression is an expression that evaluates to either true or false. It can be in one of the following shapes:
#   't' that evaluates to true.
#   'f' that evaluates to false.
#   '!(subExpr)' that evaluates to the logical NOT of the inner expression subExpr.
#   '&(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical AND of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
#   '|(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical OR of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
# Given a string expression that represents a boolean expression, return the evaluation of that expression.
# It is guaranteed that the given expression is valid and follows the given rules.

def parseBoolExpr(expression):
    stack = []

    for i in expression:
        if i != ")":
            stack.append(i)
        else:
            curStack = []
            while stack[-1] != "(":
                x = stack.pop()

                if x == "f" or x == "t":
                    curStack.append(x)
            
            stack.pop()
            operator = stack.pop()

            if (operator == "|" and curStack.count("t") >= 1) or (operator == "&" and curStack.count("t") == len(curStack)) or (operator == "!" and curStack[0] == 'f'):
                stack.append("t")
            elif (operator == "|" and curStack.count("t") == 0) or (operator == "&" and curStack.count("t") != len(curStack)) or (operator == "!" and curStack[0] == "t"):
                stack.append("f")

    if stack[0] == "t":
        return True 
    return False 

# Test cases
expression = "&(|(f))"
print(parseBoolExpr(expression))

expression = "|(f,f,f,t)"
print(parseBoolExpr(expression))

expression = "!(&(f,t))"
print(parseBoolExpr(expression))
