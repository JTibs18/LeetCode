# Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.
# In the American keyboard:
#   the first row consists of the characters "qwertyuiop",
#   the second row consists of the characters "asdfghjkl", and
#   the third row consists of the characters "zxcvbnm".

def findWords(words):
    row1 = "qwertyuiop"
    row2 = "asdfghjkl"
    row3 = "zxcvbnm"
    typed = []

    for w in words:
        sameLine = True
        if w[0].lower() in row1:
            for char in w:
                if char.lower() not in row1:
                    sameLine = False
                    break
        elif w[0].lower() in row2:
            for char in w:
                if char.lower() not in row2:
                    sameLine = False
                    break
        elif w[0].lower() in row3:
            for char in w:
                if char.lower() not in row3:
                    sameLine = False
                    break
        if sameLine == True:
            typed.append(w)
    return typed

#Test Cases
words = ["Hello","Alaska","Dad","Peace"]
print(findWords(words))

words = ["omk"]
print(findWords(words))

words = ["adsdf","sfd"]
print(findWords(words))
