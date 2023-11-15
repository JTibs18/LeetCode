# International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows:
#   'a' maps to ".-",
#   'b' maps to "-...",
#   'c' maps to "-.-.", and so on.
# For convenience, the full table for the 26 letters of the English alphabet is given below:
# [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
# Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter.
# For example, "cab" can be written as "-.-..--...", which is the concatenation of "-.-.", ".-", and "-...". We will call such a concatenation the transformation of a word.
# Return the number of different transformations among all words we have.

from collections import Counter

# slower and takes more memory
def uniqueMorseRepresentationsV1(words):
    encodings = {
        "a":".-",
        "b":"-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--.."
    }

    uniqueWordCount = set()
    encoded = ''
    
    for i in words:
        for j in i:
            encoded += encodings[j]

        uniqueWordCount.add(encoded)
        encoded = ''

    return len(uniqueWordCount)

# faster and takes less memory
def uniqueMorseRepresentations(words):
    encodings = {
        "a":".-",
        "b":"-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--.."
    }
    
    return len(Counter(''.join(map(lambda c: encodings[c], word)) for word in words))

# Test cases
words = ["gin","zen","gig","msg"]
print(uniqueMorseRepresentations(words))

words = ["a"]
print(uniqueMorseRepresentations(words))
