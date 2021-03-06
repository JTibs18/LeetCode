# A sentence 'sentence' is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.
# We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)

# The rules of Goat Latin are as follows:
# If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
# For example, the word 'apple' becomes 'applema'.
# If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
# For example, the word "goat" becomes "oatgma".
# Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
# For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.
# Return the final sentence representing the conversion from sentence to Goat Latin.

# Example 1:
# Input: sentence = "I speak Goat Latin"
# Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"

# Example 2:
# Input: sentence = "The quick brown fox jumped over the lazy dog"
# Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"

def goatLatin(sentence):
    s = ""
    words = sentence.split(" ")
    for index, value in enumerate(words):
        if (value[0].lower() == 'a' or value[0].lower() == 'e' or value[0].lower() == 'i' or value[0].lower() == 'u' or value[0].lower() == 'o'):
            words[index] = value + "ma"
        else:
            words[index] = value[1:] + value[0] + "ma"
        words[index] = words[index] + "a" * (index + 1)
        if (index == 0):
            s = s + words[index]
        else:
            s = s + " " + words[index]
    return s

#test cases
sentence = "I speak Goat Latin"
print(goatLatin(sentence))

sentence = "The quick brown fox jumped over the lazy dog"
print(goatLatin(sentence))
