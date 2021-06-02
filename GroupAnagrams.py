# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]

def GroupAnagram(strs):
    anagram = {}
    for index, value in enumerate(strs):
        if (tuple(sorted(value)) in anagram.keys()):
            updatedList = anagram.get(tuple(sorted(value)))
            updatedList.append(value)
            anagram[tuple(sorted(value))] = updatedList
        else:
            newList = list()
            newList.append(value)
            anagram[tuple(sorted(value))] = newList
    return list(anagram.values())


#Test cases
strs = ["eat","tea","tan","ate","nat","bat"]
print(GroupAnagram(strs))

strs = [""]
print(GroupAnagram(strs))

strs = ["a"]
print(GroupAnagram(strs))
