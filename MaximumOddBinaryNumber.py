# You are given a binary string s that contains at least one '1'.
# You have to rearrange the bits in such a way that the resulting binary number is the maximum odd binary number that can be created from this combination.
# Return a string representing the maximum odd binary number that can be created from the given combination.
# Note that the resulting string can have leading zeros.

def maximumOddBinaryNumber(s):
    if s.count("1") == 1 and s[-1] == "1":
        return s
    elif s.count("1") == 1:
        return ("0" * (len(s) - 1)) + "1"
    
    return ("1" * (s.count("1") - 1)) + ("0" * (s.count("0"))) + "1"

# Test cases
s = "010"
print(maximumOddBinaryNumber(s))

s = "0101"
print(maximumOddBinaryNumber(s))

s = "111"
print(maximumOddBinaryNumber(s))
