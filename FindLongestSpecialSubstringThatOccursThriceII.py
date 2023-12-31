# You are given a string s that consists of lowercase English letters.
# A string is called special if it is made up of only a single character. For example, the string "abc" is not special, whereas the strings "ddd", "zz", and "f" are special.
# Return the length of the longest special substring of s which occurs at least thrice, or -1 if no special substring occurs at least thrice.
# A substring is a contiguous non-empty sequence of characters within a string.
# For Weekly Contest 378 Question #3

def maximumLength(s):
    letterDict = dict()
    maxLen = -1

    for indx, val in enumerate(s):
        if val not in letterDict:
            letterDict[val] = [indx]
        else:
            letterDict[val].append(indx)

    for value in letterDict.values():
        curMax = 1
        distances = []
        distanceCount = dict()

        for i in range(1, len(value)):
            if value[i] == value[i - 1] + 1:
                curMax += 1 
            else: 
                distances.append(curMax)
                curMax = 1
        distances.append(curMax)


        for i in distances:
            if i not in distanceCount:
                distanceCount[i] = 1
            else:
                distanceCount[i] += 1

        distanceOccurrences = sorted(distanceCount.items(), key=lambda x: (x[0]), reverse=True)
        prev = 0

        for length, freq in distanceOccurrences: 
            if freq >= 3 and length > maxLen:
                maxLen = length 
            elif freq == 2 and length != 1 and length - 1 > maxLen:
                maxLen = length - 1 
            elif length > 3 and length - 2 > maxLen and prev == 0:
                maxLen = length - 2 
            elif (sum(distances) > 2 and maxLen < max(distances) - 2):
                maxLen = max(distances) - 2 
            elif length > 1 and length > maxLen and prev > 0:
                maxLen = length 

            if maxLen == 0:
                maxLen = 1 
            prev += 1 

    return maxLen

# Test cases
s = "aaaa"
print(maximumLength(s))

s = "abcdef"
print(maximumLength(s))

s = "abcaba"
print(maximumLength(s))

s = "jinhhhtttttttefffffjjjjjjjjjfffffjjjjjjjjjqvvvvvvg"
print(maximumLength(s))
