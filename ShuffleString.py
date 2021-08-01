# Given a string s and an integer array indices of the same length.
# The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
# Return the shuffled string.

def restoreString(s, indices):
    ans = [None] * len(s)
    a = ""

    for indx, char in enumerate(s):
        ans[indices[indx]] = char

    return a.join(ans)

#Test cases
s = "codeleet"
indices = [4, 5, 6, 7, 0, 2, 1, 3]
print(restoreString(s, indices))

s = "abc"
indices = [0, 1, 2]
print(restoreString(s, indices))

s = "aiohn"
indices = [3,1,4,2,0]
print(restoreString(s, indices))

s = "aaiougrt"
indices = [4,0,2,6,7,3,1,5]
print(restoreString(s, indices))

s = "art"
indices = [1,0,2]
print(restoreString(s, indices))
