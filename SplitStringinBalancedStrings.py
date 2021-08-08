# Balanced strings are those that have an equal quantity of 'L' and 'R' characters.
# Given a balanced string s, split it in the maximum amount of balanced strings.
# Return the maximum amount of split balanced strings.

def balancedStringSplit(s):
    count = 0
    stack = []

    for lr in s:
        if stack == []:
            stack.append(lr)
        elif lr == stack[0]:
            stack.append(lr)
        else:
            stack.pop()
            if stack == []:
                count += 1

    return count

#Test cases
s = "RLRRLLRLRL"
print(balancedStringSplit(s))

s = "RLLLLRRRLR"
print(balancedStringSplit(s))

s = "LLLLRRRR"
print(balancedStringSplit(s))

s = "RLRRRLLRLL"
print(balancedStringSplit(s))
