# Given an array of strings words and a character separator, split each string in words by separator.
# Return an array of strings containing the new strings formed after the splits, excluding empty strings.
# Notes
#   separator is used to determine where the split should occur, but it is not included as part of the resulting strings.
#   A split may result in more than two strings.
#   The resulting strings must maintain the same order as they were initially given.

def splitWordsBySeparator(words, separator):
    returnWords = []

    for i in words:
        returnWords.extend(x for x in i.split(separator) if x != "")

    return returnWords

# Test cases
words = ["one.two.three","four.five","six"]
separator = "."
print(splitWordsBySeparator(words, separator))

words = ["$easy$","$problem$"]
separator = "$"
print(splitWordsBySeparator(words, separator))

words = ["|||"]
separator = "|"
print(splitWordsBySeparator(words, separator))
