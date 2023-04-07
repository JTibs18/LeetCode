# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
# You can use each character in text at most once. Return the maximum number of instances that can be formed.

def maxNumberOfBalloons(text):
    letterCount = dict()
    count = 0 

    for i in text: 
        if i in letterCount: 
            letterCount[i] += 1 
        else:
            letterCount[i] = 1

    while True: 
        if "b" in letterCount and "a" in letterCount and "l" in letterCount and "o" in letterCount and "n" in letterCount and letterCount["b"] >= 1 and letterCount["a"] >= 1 and letterCount["l"] >= 2 and letterCount["o"] >= 2 and letterCount["n"] >= 1: 
            letterCount["b"] -= 1
            letterCount["a"] -= 1 
            letterCount["l"] -= 2
            letterCount["o"] -= 2
            letterCount["n"] -= 1
            count += 1 
        else: 
            break
            
    return count 

# Test cases
text = "nlaebolko"
print(maxNumberOfBalloons(text))

text = "loonbalxballpoon"
print(maxNumberOfBalloons(text))

text = "leetcode"
print(maxNumberOfBalloons(text))
