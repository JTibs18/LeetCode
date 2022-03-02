# You are given an array of strings words and a string pref.
# Return the number of strings in words that contain pref as a prefix.
# A prefix of a string s is any leading contiguous substring of s.

def prefixCount(words, pref):
    length = len(pref)
    count = 0

    for i in words:
        if pref == i[:length]:
            count += 1

    return count

#Test Cases
words = ["pay","attention","practice","attend"]
pref = "at"
print(prefixCount(words, pref))

words = ["leetcode","win","loops","success"]
pref = "code"
print(prefixCount(words, pref))
