# Given a binary string s ​​​​​without leading zeros, return true​​​ if s contains at most one contiguous segment of ones. Otherwise, return false.

def checkOnesSegment(s):
    conOnes = 0

    for num in s:
        if int(num) == 1:
            if conOnes == -1:
                return False
            conOnes += 1
        else:
            conOnes = -1

    return True

#Test Cases
s = "1001"
print(checkOnesSegment(s))

s = "110"
print(checkOnesSegment(s))

s = "1"
print(checkOnesSegment(s))

s = "10"
print(checkOnesSegment(s))
