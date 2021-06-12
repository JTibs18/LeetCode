# Given a string s consisting only of characters 'a', 'b', and 'c'. You are asked to apply the following algorithm on the string any number of times:
    # Pick a non-empty prefix from the string s where all the characters in the prefix are equal.
    # Pick a non-empty suffix from the string s where all the characters in this suffix are equal.
    # The prefix and the suffix should not intersect at any index.
    # The characters from the prefix and suffix must be the same.
    # Delete both the prefix and the suffix.
    # Return the minimum length of s after performing the above operation any number of times (possibly zero times).

def minimumLength(s):
    p1 = 0
    p2 = len(s) - 1
    change = 0
    while (p1 < len(s)):
        if s[p1] == s[p2] and p1 != p2:
            prev1 = p1
            prev2 = p2
            while (p1 < len(s) and s[prev1] == s[p1]):
                p1 += 1
                change += 1
            while (p2 >= 0 and s[prev2] == s[p2]):
                p2 -= 1
                change += 1
        else:
            return len(s) - change
    return 0

#test cases
s = "cabaabac"
print(minimumLength(s))

s = "ca"
print(minimumLength(s))

s = "aabccabba"
print(minimumLength(s))

s = "bbbbbbbbbbbbbbbbbbb"
print(minimumLength(s))
