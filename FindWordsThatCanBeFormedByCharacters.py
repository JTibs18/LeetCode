# You are given an array of strings words and a string chars.
# A string is good if it can be formed by characters from chars (each character can only be used once).
# Return the sum of lengths of all good strings in words.

def countCharacters(words, chars):
    charsCount = dict()
    stringsFormed = 0 

    for i in chars: 
        if i in charsCount:
            charsCount[i] += 1
        else: 
            charsCount[i] = 1
    
    for word in words: 
        letterCount = dict()

        for i in word: 
            if i in letterCount:
                letterCount[i] += 1
            else:
                letterCount[i] = 1

        validWord = True 
        for key, value in letterCount.items():
            if key not in charsCount or charsCount[key] < value:
                validWord = False
                break 

        if validWord:
            stringsFormed += len(word)

    return stringsFormed

# Test cases
words = ["cat","bt","hat","tree"]
chars = "atach"
print(countCharacters(words, chars))

words = ["hello","world","leetcode"]
chars = "welldonehoneyr"
print(countCharacters(words, chars))
