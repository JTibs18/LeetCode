# You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.
# We repeatedly make duplicate removals on s until we no longer can.
# Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique

def removeDuplicates(s): 
    letterStack = ""

    for i in s: 
        if len(letterStack) > 0 and i == letterStack[len(letterStack) - 1]:
            letterStack = letterStack[:-1]
        else: 
            letterStack +=  i

    return letterStack

# Test cases
s = "abbaca"
print(removeDuplicates(s))

s = "azxxzy"
print(removeDuplicates(s))
