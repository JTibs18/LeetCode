# Write a function that reverses a string. The input string is given as an array of characters s.

# Example 1:
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]


# Example 2:
# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

def revString(s):
    return (list(reversed(s)))
#Note: Leetcode prefers s.reverse() with no return statement


#test cases
s = ["h","e","l","l","o"]
print(revString(s))

s = ["H","a","n","n","a","h"]
print(revString(s))
