# You are given a character array keys containing unique characters and a string array values containing strings of length 2. You are also given another string array dictionary that contains all permitted original strings after decryption. You should implement a data structure that can encrypt or decrypt a 0-indexed string.
# A string is encrypted with the following process:
#   1. For each character c in the string, we find the index i satisfying keys[i] == c in keys.
#   2. Replace c with values[i] in the string.
# Note that in case a character of the string is not present in keys, the encryption process cannot be carried out, and an empty string "" is returned.
# A string is decrypted with the following process:
#   1. For each substring s of length 2 occurring at an even index in the string, we find an i such that values[i] == s. If there are multiple valid i, we choose any one of them. This means a string could have multiple possible strings it can decrypt to.
#   2. Replace s with keys[i] in the string.
# Implement the Encrypter class:
#   Encrypter(char[] keys, String[] values, String[] dictionary) Initializes the Encrypter class with keys, values, and dictionary.
#   String encrypt(String word1) Encrypts word1 with the encryption process described above and returns the encrypted string.
#   int decrypt(String word2) Returns the number of possible strings word2 could decrypt to that also appear in dictionary.

class Encrypter: 
    def __init__(self, keys, values, dictionary):
        self.encryptDict = dict()
        self.dictionary = dictionary

        for indx, val in enumerate(keys):
            self.encryptDict[val] = values[indx]

    def encrypt(self, word1):
        word = ''

        for c in word1:
            if c not in self.encryptDict:
                return ''
            word += self.encryptDict[c]

        return word

    def decrypt(self, word2):
        possibleWords = 0

        for i in self.dictionary:
            if word2 == self.encrypt(i):
                possibleWords += 1 
            
        return possibleWords

# Test case
keys = ['a', 'b', 'c', 'd']
values = ["ei", "zf", "ei", "am"]
dictionary = ["abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda", "abad"]
encrypter = Encrypter(keys, values, dictionary)
print(encrypter.encrypt("abcd"))
print(encrypter.decrypt("eizfeiam"))
