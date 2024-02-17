# You are given a string s.
# Consider performing the following operation until s becomes empty:
#   For every alphabet character from 'a' to 'z', remove the first occurrence of that character in s (if it exists).
# For example, let initially s = "aabcbbca". We do the following operations:
#   Remove the underlined characters s = "aabcbbca". The resulting string is s = "abbca".
#   Remove the underlined characters s = "abbca". The resulting string is s = "ba".
#   Remove the underlined characters s = "ba". The resulting string is s = "".
# Return the value of the string s right before applying the last operation. In the example above, answer is "ba".
# For Biweekly Contest #124 Question 2

def lastNonEmptyString1(s: str) -> str:
    while len(set(s)) != len(s):
        removedSet = set()
        newS = ""
        
        for i in s:
            if i not in removedSet:
                removedSet.add(i)
            else:
                newS += i 

        s = newS
        
    return s

def lastNonEmptyString(s):
    s = s[::-1]
    foundSet = set()
    newS = ""
    foundChar = dict()

    for i in s:
        if i not in foundChar:
            foundChar[i] = 1
        else:
            foundChar[i] += 1 

    for i in s: 
        if i not in foundSet and foundChar[i] == max(foundChar.values()):
            newS += i
            foundSet.add(i)

    return newS[::-1]
        

# Test cases
s = "aabcbbca"
print(lastNonEmptyString(s))

s = "abcd"
print(lastNonEmptyString(s))
