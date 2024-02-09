# You are given a license key represented as a string s that consists of only alphanumeric characters and dashes. The string is separated into n + 1 groups by n dashes. You are also given an integer k.
# We want to reformat the string s such that each group contains exactly k characters, except for the first group, which could be shorter than k but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.
# Return the reformatted license key.

def licenseKeyFormatting(s, k):
    parsed = "".join(s.split("-"))
    lenParsed = len(parsed)

    for i in range(lenParsed - k, 0, -k):
        parsed = parsed[:i] + "-" + parsed[i:]
    
    return parsed.upper()

# Test cases
s = "5F3Z-2e-9-w"
k = 4
print(licenseKeyFormatting(s, k))

s = "2-5g-3-J"
k = 2
print(licenseKeyFormatting(s, k))
