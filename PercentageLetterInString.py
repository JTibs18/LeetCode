# Given a string s and a character letter, return the percentage of characters in s that equal letter rounded down to the nearest whole percent.

from collections import Counter

# slowest 
def percentageLetter1(s, letter): 
    counter = Counter(s)
    return int((counter[letter] / len(s)) * 100)

# fastest solution, same amount of memory usage as first attempt
def percentageLetter2(s, letter): 
    lenCount = 0 
    count = 0 

    for i in s: 
        lenCount += 1 
        if i == letter: 
            count += 1 

    return int((count / lenCount) * 100)

# second fastest and least amount of memory 
def percentageLetter(s, letter): 
    count = 0 

    for i in s: 
        if i == letter: 
            count += 1 

    return int((count / len(s)) * 100)

# Test cases
s = "foobar"
letter = "o"
print(percentageLetter(s, letter))

s = "jjjj" 
letter = "k"
print(percentageLetter(s, letter))
