# You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.
# Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.
# Return any permutation of s that satisfies this property.

def customSortString(order, s):
    return "".join(sorted(s, key=lambda word: [order.index(c) if c in order else len(order) + 1 for c in word]))

# Test cases
order = "cba"
s = "abcd"
print(customSortString(order, s))

order = "cbafg"
s = "abcd"
print(customSortString(order, s))
