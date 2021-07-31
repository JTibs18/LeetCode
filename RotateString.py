# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
# A shift on s consists of moving the leftmost character of s to the rightmost position.
# For example, if s = "abcde", then it will be "bcdea" after one shift.

def rotateString(s, goal):
    chars = list(s)

    for i in range(len(s) + 1):
        newS = ""
        if newS.join(chars) == goal:
            return True
        else:
            chars.append(chars.pop(0))
    return False

#Test Cases
s = "abcde"
goal = "cdeab"
print(rotateString(s, goal))

s = "abcde"
goal = "abced"
print(rotateString(s, goal))
