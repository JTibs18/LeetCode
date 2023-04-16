# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.

def lengthOfLastWord(s): 
    words = s.strip().split(" ")
    return len(words[len(words) - 1])

# Test cases
s = "Hello World"
print(lengthOfLastWord(s))

s = "   fly me   to   the moon  "
print(lengthOfLastWord(s))

s = "luffy is still joyboy"
print(lengthOfLastWord(s))
