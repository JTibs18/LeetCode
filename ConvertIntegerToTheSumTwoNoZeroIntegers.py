# No-Zero integer is a positive integer that does not contain any 0 in its decimal representation.
# Given an integer n, return a list of two integers [A, B] where:
# A and B are No-Zero integers.
# A + B = n
# The test cases are generated so that there is at least one valid solution. If there are many valid solutions you can return any of them.

def getNoZeroIntegers(n):
    A = n - 1
    B = 1

    while "0" in str(A) or "0" in str(B):
        if "0" in str(A):
            B += 11 ** (len(str(A)) - (str(A).find("0") + 1))
            A -= 11 ** (len(str(A)) - (str(A).find("0") + 1))
        if "0" in str(B):
            A += 11 ** (len(str(B)) - (str(B).find("0") + 1))
            B -= 11 ** (len(str(B)) - (str(B).find("0") + 1))

    return [A, B]
#Test Cases
n = 2
print(getNoZeroIntegers(n))

n = 11
print(getNoZeroIntegers(n))

n = 101
print(getNoZeroIntegers(n))

n = 1057
print(getNoZeroIntegers(n))

n = 9095
print(getNoZeroIntegers(n))
