# You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.
# Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.
# Return true if a and b are alike. Otherwise, return false.

def halvesAlike(s):
    fCount = 0
    sCount = 0

    half = int(len(s) / 2)

    for i, char in enumerate(s):
        if i < half and (char.lower() == "a" or char.lower() == "e" or char.lower() == "i" or char.lower() == "u" or char.lower() == "o"):
            fCount += 1
        elif i >= half and (char.lower() == "a" or char.lower() == "e" or char.lower() == "i" or char.lower() == "u" or char.lower() == "o"):
            sCount += 1

    return fCount == sCount
    
#Test cases
s = "book"
print(halvesAlike(s))

s = "textbook"
print(halvesAlike(s))

s = "MerryChristmas"
print(halvesAlike(s))

s = "AbCdEfGh"
print(halvesAlike(s))
