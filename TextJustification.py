# Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.
# You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.
# Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
# For the last line of text, it should be left-justified, and no extra space is inserted between words.
# Note:
#   A word is defined as a character sequence consisting of non-space characters only.
#   Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
#   The input array words contains at least one word.

# very fast runtime, need to improve memory usage
def fullJustify(words, maxWidth):
    curLine = ''
    curWidth = 0
    curWords = []
    justifiedText = []

    for word in words:
        if len(word) + curWidth > maxWidth:
            spaces = maxWidth - (curWidth - len(curWords))

            if len(curWords) == 1: 
                numSpacesBetweenWords = spaces
            else:
                numSpacesBetweenWords = spaces // (len(curWords) - 1)

            for indx, val in enumerate(curWords):
                if indx == 0 and len(curWords) == 1:
                    curLine += val + (' ' * numSpacesBetweenWords)
                elif indx == len(curWords) - 1:
                    curLine += val
                elif spaces % (len(curWords) - 1) > 0: 
                    curLine += val + (" " * (numSpacesBetweenWords + 1))
                    spaces -= 1
                else:
                    curLine += val + (' ' * numSpacesBetweenWords)

            justifiedText.append(curLine)
            curLine = ''
            curWidth = 0
            curWords = []
        
        curWidth += len(word) + 1
        curWords.append(word)
    
    curLine += ' '.join(curWords)
    justifiedText.append(curLine + ' ' * (maxWidth - (curWidth - 1)))
    
    return justifiedText

# Test cases
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
print(fullJustify(words, maxWidth))

words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
print(fullJustify(words, maxWidth))

words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
print(fullJustify(words, maxWidth))
