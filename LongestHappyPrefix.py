# A string is called a happy prefix if is a non-empty prefix which is also a suffix (excluding itself).
# Given a string s, return the longest happy prefix of s. Return an empty string "" if no such prefix exists.

# naive solution
def longestPrefix1(s):
    prefix = ''
    suffix = ''
    ptr = 0
    longest = ""

    while ptr < len(s) - 1:
        prefix += s[ptr]
        suffix = s[len(s) - 1 - ptr] + suffix

        if prefix == suffix:
            longest = prefix
        
        ptr += 1 

    return longest

# faster and more memory efficient solution
def longestPrefix(s):
    prefix = s[1:]
    suffix = s[:-1]

    while prefix != suffix:
        prefix = prefix[1:]
        suffix = suffix[:-1]
        
    return prefix

# Test cases
s = "level"
print(longestPrefix(s))

s = "ababab"
print(longestPrefix(s))
