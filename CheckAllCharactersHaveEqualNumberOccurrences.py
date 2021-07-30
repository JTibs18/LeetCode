# Given a string s, return true if s is a good string, or false otherwise.
# A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).

def areOccurrencesEqual(s):
    characterCounts = dict()
    for char in s:
        if char not in characterCounts:
            characterCounts[char] = 1
        else:
            characterCounts[char] += 1
    prevCount = 0

    for key, val in characterCounts.items():
        if prevCount == 0:
            prevCount = val
        elif prevCount != val:
            return False
    return True

#Test Cases
s = "abacbc"
print(areOccurrencesEqual(s))

s = "aaabb"
print(areOccurrencesEqual(s))
