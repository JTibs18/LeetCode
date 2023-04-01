# Given a string of English letters s, return the greatest English letter which occurs as both a lowercase and uppercase letter in s. The returned letter should be in uppercase. If no such letter exists, return an empty string.
# An English letter b is greater than another letter a if b appears after a in the English alphabet.

def greatestLetter(s): 
    greatestLetter = "0"

    for i in set(s):
        if ((i.isupper() and i.lower() in s) or (i.islower() and i.upper() in s)) and ord(greatestLetter) < ord(i.upper()): 
            greatestLetter = i.upper() 

    if greatestLetter == "0": 
        return ""  
    return greatestLetter

# Test cases
s = "lEeTcOdE"
print(greatestLetter(s))

s = "arRAzFif"
print(greatestLetter(s))

s = "AbCdEfGhIjK"
print(greatestLetter(s))
