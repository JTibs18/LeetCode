# Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).
# The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.
# With help from: https://stackoverflow.com/questions/1779286/swapping-1-with-0-and-0-with-1-in-a-pythonic-way 

def maxScore(s):
    split = 1
    right = sum(int(x) for x in s[split:])
    left = 1 - int(s[0])
    highScore = right + left 

    while split < len(s) - 1: 
        nextNum = int(s[split])
        right -= nextNum
        left += 1 - nextNum
        highScore = max(highScore, right + left)
        split += 1

    return highScore

# Test cases
s = "011101"
print(maxScore(s))

s = "00111"
print(maxScore(s))

s = "1111"
print(maxScore(s))

s = "01001"
print(maxScore(s))