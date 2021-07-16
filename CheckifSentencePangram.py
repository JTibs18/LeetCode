# A pangram is a sentence where every letter of the English alphabet appears at least once.
# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

#Using list to store unique characters
def checkIfPangram(sentence):
    letters = []

    if len(sentence) < 26:
        return False

    for char in sentence:
        if char not in letters:
            letters.append(char)

    if len(letters) == 26:
        return True
    else:
        return False

#Using set to store unique characters
def checkIfPangram2(sentence):
    letters = set()

    if len(sentence) < 26:
        return False

    for char in sentence:
        letters.add(char)

    if len(letters) == 26:
        return True
    else:
        return False

#Test cases
sentence = "thequickbrownfoxjumpsoverthelazydog"
print(checkIfPangram(sentence))
print(checkIfPangram2(sentence))

sentence = "leetcode"
print(checkIfPangram(sentence))
print(checkIfPangram2(sentence))

sentence = "uwqohxamknblecdtzpisgvyfjr"
print(checkIfPangram(sentence))
print(checkIfPangram2(sentence))
