# Given a pattern and a string s, find if s follows the same pattern.
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

def wordPattern(pattern, s): 
    patternMapping = dict()
    sentence = s.split(" ")

    if len(sentence) != len(pattern): 
        return False

    for indx, val in enumerate(pattern): 
        if val in patternMapping: 
            if patternMapping[val] != sentence[indx]: 
                return False 
        elif sentence[indx] not in patternMapping.values(): 
            patternMapping[val] = sentence[indx]
        else: 
            return False 

    return True

# Test cases 
pattern = "abba"
s = "dog cat cat dog"
print(wordPattern(pattern, s))

pattern = "abba"
s = "dog cat cat fish"
print(wordPattern(pattern, s))

pattern = "aaaa"
s = "dog cat cat dog"
print(wordPattern(pattern, s))

pattern = "abba" 
s = "dog dog dog dog"
print(wordPattern(pattern, s))

pattern = "aaa"
s = "aa aa aa aa"
print(wordPattern(pattern, s))
