# You are given a string containing only 4 kinds of characters 'Q', 'W', 'E' and 'R'.
# A string is said to be balanced if each of its characters appears n/4 times where n is the length of the string.
# Return the minimum length of the substring that can be replaced with any other string of the same length to make the original string s balanced.
# Return 0 if the string is already balanced.

def balancedString(s):
    charactersDict = {}
    n = len(s)
    appear = n / 4
    for letter in s:
        if letter in charactersDict.keys():
            val = charactersDict.get(letter)
            val += 1
            charactersDict[letter] = val
        else:
            newLetter = {letter : 1}
            charactersDict.update(newLetter)
    if appear == max(charactersDict.values()):
        return 0
    else:
        letterFlip = 0
        keys = []
        for value in charactersDict.values():
            if value > appear:
                diff = value - appear
                letterFlip = letterFlip + diff
                # for key, val in charactersDict.items():
                #     if value == val:
                #         keys.append(key)
        return letterFlip

#Test cases
s = "QWER"
print(balancedString(s))

s = "QWQE"
print(balancedString(s))

s = "QQQW"
print(balancedString(s))

s = "QQQQ"
print(balancedString(s))

s = "WQWRQQQW"
print(balancedString(s))


#PROBLEM WITH THIS CASE. SHOULD RETURN 4, not 3. USE SLIDING WINDOW TO FIND LONGEST STREAK TO REPLACE, NOT JUST # of characters to replace
s = "WWEQERQWQWWRWWERQWEQ"
print(balancedString(s))
