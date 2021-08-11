# Given a non-empty list of words, return the k most frequent elements.
# Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

def topKFrequent(words, k):
    wordDic = dict()

    for w in words:
        if w in wordDic:
            wordDic[w] += 1
        else:
            wordDic[w] = 1

    return [key for key,value in sorted(wordDic.items(), key=lambda x: (-x[1], x[0]))][:k]

#Test Cases
words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
print(topKFrequent(words, k))

words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4
print(topKFrequent(words, k))

words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 3
print(topKFrequent(words, k))
