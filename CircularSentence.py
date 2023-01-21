# A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
# For example, "Hello World", "HELLO", "hello world hello world" are all sentences.
# Words consist of only uppercase and lowercase English letters. Uppercase and lowercase English letters are considered different.
# A sentence is circular if:
# The last character of a word is equal to the first character of the next word.
# The last character of the last word is equal to the first character of the first word.
# For example, "leetcode exercises sound delightful", "eetcode", "leetcode eats soul" are all circular sentences. However, "Leetcode is cool", "happy Leetcode", "Leetcode" and "I like Leetcode" are not circular sentences.
# Given a string sentence, return true if it is circular. Otherwise, return false.

def isCircularSentence(sentence): 
    sentence = sentence.split(" ")
    
    if len(sentence) < 2: 
        if sentence[0][0] == sentence[0][len(sentence[0]) - 1]: 
            return True 
        else: 
            return False 
    
    for indx, val in enumerate(sentence): 
        if indx + 1 < len(sentence): 
            if val[len(val) - 1] != sentence[indx + 1][0]: 
                return False 
        else: 
            if val[len(val) - 1] != sentence[0][0]: 
                return False 
    
    return True 

# Test cases 
sentence = "leetcode exercises sound delightful"
print(isCircularSentence(sentence))

sentence = "eetcode"
print(isCircularSentence(sentence))

sentence = "Leetcode is cool"
print(isCircularSentence(sentence))

sentence = "leetcode"
print(isCircularSentence(sentence))
