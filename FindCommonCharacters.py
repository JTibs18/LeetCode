# Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

def commonChars(words):
    letterCount = dict()
    minFrequencyPerLetter = dict()
    commonCharacters = []

    for word in words: 
        wordSet = set(word)
        
        for c in wordSet: 
            if c in letterCount: 
                letterCount[c] += 1
            else: 
                letterCount[c] = 1 
            letterFrequency = word.count(c)

            if (c in minFrequencyPerLetter and letterFrequency < minFrequencyPerLetter[c]) or c not in minFrequencyPerLetter:
                minFrequencyPerLetter[c] = letterFrequency

    for key, value in letterCount.items(): 
        
        if value == len(words):
            commonCharacters.extend(", ".join([key * minFrequencyPerLetter[key]]))

    return commonCharacters

# Test cases
words = ["bella","label","roller"] # NOT WORKING FOR DUPLICATES
print(commonChars(words))

words = ["cool","lock","cook"]
print(commonChars(words))
