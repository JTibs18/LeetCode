# A sentence is a string of single-space separated words where each word consists only of lowercase letters.
# A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
# Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

def uncommonFromSentences(s1, s2):
    words = s1.split()
    words.extend(s2.split())
    wordCount = dict()
    uncommonWords = []

    for w in words:
        if w not in wordCount:
            wordCount[w] = 1
        else:
            wordCount[w] += 1

    for key, val in wordCount.items():
        if val == 1:
            uncommonWords.append(key)

    return uncommonWords

#Test Cases
s1 = "this apple is sweet"
s2 = "this apple is sour"
print(uncommonFromSentences(s1, s2))

s1 = "apple apple"
s2 = "banana"
print(uncommonFromSentences(s1, s2))
