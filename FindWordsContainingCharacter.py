# You are given a 0-indexed array of strings words and a character x.
# Return an array of indices representing the words that contain the character x.
# Note that the returned array may be in any order.

def findWordsContaining(words, x):
    wordsContainingChar = []

    for indx, val in enumerate(words):
        if x in val:
            wordsContainingChar.append(indx)

    return wordsContainingChar 

# Test cases
words = ["leet","code"]
x = "e"
print(findWordsContaining(words, x))

words = ["abc","bcd","aaaa","cbc"]
x = "a"
print(findWordsContaining(words, x))

words = ["abc","bcd","aaaa","cbc"]
x = "z"
print(findWordsContaining(words, x))
