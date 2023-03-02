# Given an array of characters chars, compress it using the following algorithm:
# Begin with an empty string s. For each group of consecutive repeating characters in chars:
# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.
# After you are done modifying the input array, return the new length of the array.
# You must write an algorithm that uses only constant extra space.

# faster algorithm but takes more space
def compress(chars): 
    s = ''
    prevChar = ''
    charCount = 0

    for i in chars: 
        if prevChar == '': 
            prevChar = i 
            charCount += 1 
        elif prevChar == i: 
            charCount += 1 
        else: 
            if charCount == 1: 
                s += prevChar
                prevChar = i 
            else: 
                s += prevChar + str(charCount)
                prevChar = i 
                charCount = 1
    
    if charCount == 1: 
        s += prevChar
    else: 
        s += prevChar + str(charCount) 
    
    chars[:] = list(s)

    return len(s)

# slower algorithm but takes less space
def compress1(chars): 
    s = ''
    indx = -1
    charCount = 0

    for i in chars: 
        if indx == -1: 
            charCount += 1 
        elif chars[indx] == i: 
            charCount += 1 
        else: 
            if charCount == 1: 
                s += chars[indx]
            else: 
                s += chars[indx] + str(charCount)
                charCount = 1
        indx += 1 
    
    if charCount == 1: 
        s += chars[indx]
    else: 
        s += chars[indx] + str(charCount) 
    
    chars[:] = list(s)

    return len(s)

# Test cases
chars = ["a","a","b","b","c","c","c"]
print(compress(chars))

chars = ["a"]
print(compress(chars))

chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
print(compress(chars))
