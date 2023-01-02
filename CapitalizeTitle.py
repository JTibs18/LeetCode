# You are given a string title consisting of one or more words separated by a single space, where each word consists of English letters. Capitalize the string by changing the capitalization of each word such that:
# If the length of the word is 1 or 2 letters, change all letters to lowercase.
# Otherwise, change the first letter to uppercase and the remaining letters to lowercase.
# Return the capitalized title.

def capitalizeTitle(title): 
    titleWords = title.split(" ")
    newTitle = ""

    for word in titleWords: 
        if len(word) > 2: 
            word = word[0].upper() + word[1:].lower()
        else: 
            word = word.lower()
        newTitle += word + " "

    return newTitle.strip()            

# Test cases 
title = "capiTalIze tHe titLe"
print(capitalizeTitle(title))

title = "First leTTeR of EACH Word"
print(capitalizeTitle(title))

title = "i lOve leetcode"
print(capitalizeTitle(title))
