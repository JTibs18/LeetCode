# You are given a 0-indexed string word and an integer k.
# At every second, you must perform the following operations:
# Remove the first k characters of word.
# Add any k characters to the end of word.
# Note that you do not necessarily need to add the same characters that you removed. However, you must perform both operations at every second.
# Return the minimum time greater than zero required for word to revert to its initial state.
# For Weekly Contest #383, Question 2 and 4

def minimumTimeToInitialState(word, k):
    count = 1
    indx = k 

    while indx < len(word):
        l = len(word[indx:])
        
        if word[indx:] == word[:l]:
            break 
        
        count += 1
        indx += k 
    
    return count

# Test cases
word = "abacaba"
k = 3
print(minimumTimeToInitialState(word, k))

word = "abacaba"
k = 4
print(minimumTimeToInitialState(word, k))

word = "abcbabcd"
k = 2 
print(minimumTimeToInitialState(word, k))