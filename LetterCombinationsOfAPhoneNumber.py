# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

def letterCombinations(digits):
    letterMappings = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]} 
    result = []
    track = ""
    
    if len(digits) == 0:
        return result 
    
    def backtrack(track):
        if (len(digits) == len(track)):
            result.append(track)
            return 
        
        for j in letterMappings[digits[len(track)]]:
            track += j
            backtrack(track)
            track = track[:-1]

    backtrack(track)
    return result

# Test cases
digits = "23"
print(letterCombinations(digits))

digits = ""
print(letterCombinations(digits))

digits = "2"
print(letterCombinations(digits))