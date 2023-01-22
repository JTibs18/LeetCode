# For Weekly Contest #329 Question #3
# You are given two 0-indexed binary strings s and target of the same length n. You can do the following operation on s any number of times:
# Choose two different indices i and j where 0 <= i, j < n.
# Simultaneously, replace s[i] with (s[i] OR s[j]) and s[j] with (s[i] XOR s[j]).
# For example, if s = "0110", you can choose i = 0 and j = 2, then simultaneously replace s[0] with (s[0] OR s[2] = 0 OR 1 = 1), and s[2] with (s[0] XOR s[2] = 0 XOR 1 = 1), so we will have s = "1110".
# Return true if you can make the string s equal to target, or false otherwise.

def makeStringsEqual(s, target): 
    s = sorted(s) 
    target = sorted(target)
    oneCount = 0 

    if (s == target): 
        return True 

    for i in s: 
        if i == "1": 
            oneCount += 1 

    for indx, val in enumerate(s):
        if val == "0" and target[indx] == "1": 
            if oneCount < 1: 
                return False 
            else: 
                oneCount += 1
        elif val == "1" and target[indx] == "0": 
            oneCount -= 1
            if oneCount < 1: 
                return False 
    
    return True 

# Test cases 
s = "1010"
target = "0110"
print(makeStringsEqual(s, target))

s = "11"
target = "00"
print(makeStringsEqual(s, target))

s = "001000"
target = "000100"
print(makeStringsEqual(s, target))

s = "11110"
target = "00101"
print(makeStringsEqual(s, target))
                                                                    