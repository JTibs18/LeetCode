# You are given a 0-indexed string s that has lowercase English letters in its even indices and digits in its odd indices.
# There is a function shift(c, x), where c is a character and x is a digit, that returns the xth character after c.
# For example, shift('a', 5) = 'f' and shift('x', 0) = 'x'.
# For every odd index i, you want to replace the digit s[i] with shift(s[i-1], s[i]).
# Return s after replacing all digits. It is guaranteed that shift(s[i-1], s[i]) will never exceed 'z'.

def replaceDigits(s):
    prevChar = ""
    newString = ""

    def shift(c, x):
        val = ord(c)
        newChar = val + int(x)
        return chr(newChar)

    for indx, val in enumerate(s):
        if indx % 2 == 1:
            newChar = shift(prevChar, val)
            newString += newChar
        else:
            prevChar = val
            newString += val
    return newString

#Test cases
s = "a1c1e1"
print(replaceDigits(s))

s = "a1b2c3d4e"
print(replaceDigits(s))
