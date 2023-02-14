# Given two binary strings a and b, return their sum as a binary string.

# Reference: https://www.geeksforgeeks.org/python-program-to-add-two-binary-numbers/

def addBinary(a, b): 
    return str(bin(int(a, 2) + int(b, 2)))[2:]

# Test cases
a = "11"
b = "1"
print(addBinary(a, b))

a = "1010"
b = "1011"
print(addBinary(a, b))
