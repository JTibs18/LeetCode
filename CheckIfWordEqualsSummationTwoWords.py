# The letter value of a letter is its position in the alphabet starting from 0 (i.e. 'a' -> 0, 'b' -> 1, 'c' -> 2, etc.).
# The numerical value of some string of lowercase English letters s is the concatenation of the letter values of each letter in s, which is then converted into an integer.
# For example, if s = "acb", we concatenate each letter's letter value, resulting in "021". After converting it, we get 21.
# You are given three strings firstWord, secondWord, and targetWord, each consisting of lowercase English letters 'a' through 'j' inclusive.
# Return true if the summation of the numerical values of firstWord and secondWord equals the numerical value of targetWord, or false otherwise.

def isSumEqual(firstWord, secondWord, targetWord):
    testNumOne = ''
    testNumTwo = ''
    targetNum = ''

    for i in firstWord:
        testNumOne += str(ord(i) - 97)

    for i in secondWord:
        testNumTwo += str(ord(i) - 97)


    for i in targetWord:
        targetNum += str(ord(i) - 97)

    if (int(targetNum) == (int(testNumOne) + int(testNumTwo))):
        return True
    else:
        return False 

#Test Cases
firstWord = "acb"
secondWord = "cba"
targetWord = "cdb"
print(isSumEqual(firstWord, secondWord, targetWord))



firstWord = "aaa"
secondWord = "a"
targetWord = "aab"
print(isSumEqual(firstWord, secondWord, targetWord))


firstWord = "aaa"
secondWord = "a"
targetWord = "aaaa"
print(isSumEqual(firstWord, secondWord, targetWord))
