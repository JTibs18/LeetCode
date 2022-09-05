# Given two integer arrays pushed and popped each with distinct values, return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, or false otherwise.

def validateStackSequences (pushed, popped):
    curStack = []
    poppedIndx = 0

    for i in pushed:
        curStack.append(i)
        while poppedIndx < len(popped) and len(curStack) != 0 and curStack[len(curStack) - 1] == popped[poppedIndx]:
            curStack.pop()
            poppedIndx += 1

    if len(curStack) == 0 and poppedIndx == len(popped):
        return True
    else:
        return False

#Test cases
pushed = [1, 2, 3, 4, 5]
popped = [4, 5, 3, 2, 1]
print(validateStackSequences(pushed, popped))

pushed = [1, 2, 3, 4, 5]
popped = [4, 3, 5, 1, 2]
print(validateStackSequences(pushed, popped))

pushed = [1,0]
popped = [1,0]
print(validateStackSequences(pushed, popped))
