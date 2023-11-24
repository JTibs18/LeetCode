# You are given two integers, num and t.
# An integer x is called achievable if it can become equal to num after applying the following operation no more than t times:
# Increase or decrease x by 1, and simultaneously increase or decrease num by 1.
# Return the maximum possible achievable number. It can be proven that there exists at least one achievable number.

def theMaximumAchievableX(num, t): 
    return num + (t * 2)

# Test cases
num = 4
t = 1 
print(theMaximumAchievableX(num, t))

num = 3
t = 2
print(theMaximumAchievableX(num, t))