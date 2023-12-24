# You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.
# The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.
# Return the minimum number of operations needed to make s alternating.

def minOperations(s):
    operations = 0
    num = "0"

    for i in s:
        if i != num:
            operations += 1

        num = str(1 - int(num)) 
    
    return min(len(s) - operations, operations)

# Test cases
s = "0100"
print(minOperations(s))

s = "10"
print(minOperations(s))

s = "1111"
print(minOperations(s))

s = "10010100"
print(minOperations(s))
