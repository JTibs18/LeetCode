# Given two strings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

def canConstruct(ransomNote, magazine):

    for i in ransomNote:
        if i in magazine:
            magazine = magazine.replace(i, "", 1)
        else:
            return False

    return True

#Test Cases
ransomNote = "a"
magazine = "b"
print(canConstruct(ransomNote, magazine))

ransomNote = "aa"
magazine = "ab"
print(canConstruct(ransomNote, magazine))

ransomNote = "aa"
magazine = "aab"
print(canConstruct(ransomNote, magazine))
