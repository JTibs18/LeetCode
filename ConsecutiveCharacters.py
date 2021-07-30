# Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.
# Return the power of the string.

def maxPower(s):
    prevLetter = ""
    consecutive = 1
    maxCon = 1

    for indx, val in enumerate(s):
        if indx == 0:
            prevLetter = val
        elif prevLetter == val:
            consecutive += 1
        else:
            if consecutive > maxCon:
                maxCon = consecutive
            consecutive = 1

        if consecutive > maxCon:
            maxCon = consecutive

        prevLetter = val

    return maxCon

#Test Cases
s = "leetcode"
print(maxPower(s))

s = "abbcccddddeeeeedcba"
print(maxPower(s))

s = "triplepillooooow"
print(maxPower(s))

s = "hooraaaaaaaaaaay"
print(maxPower(s))

s = "tourist"
print(maxPower(s))
