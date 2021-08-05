# Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.
# A string is represented by an array if the array elements concatenated in order forms the string.

#Faster solution, less memory efficient
def arrayStringsAreEqual(word1, word2):
    w1 = ""
    w2 = ""

    for word in word1:
        w1 = w1 + word

    for word in word2:
        w2 = w2 + word

    if w1 == w2:
        return True
    else:
        return False

#More memory efficient, slower solution
def arrayStringsAreEqual2(word1, word2):
    return "".join(word1) == "".join(word2)

#Test cases
word1 = ["ab", "c"]
word2 = ["a", "bc"]
print(arrayStringsAreEqual(word1, word2))
print(arrayStringsAreEqual2(word1, word2))

word1 = ["a", "cb"]
word2 = ["ab", "c"]
print(arrayStringsAreEqual(word1, word2))
print(arrayStringsAreEqual2(word1, word2))

word1  = ["abc", "d", "defg"]
word2 = ["abcddefg"]
print(arrayStringsAreEqual(word1, word2))
print(arrayStringsAreEqual2(word1, word2))
