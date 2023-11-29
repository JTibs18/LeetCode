# Write a function that takes the binary representation of an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

def hammingWeight(n):
    return sum([int(x) for x in bin(n)[2:]])

# Test cases
n = 0b0000000000000000000000000001011
print(hammingWeight(n))

n = 0b0000000000000000000000010000000
print(hammingWeight(n))

n = 0b11111111111111111111111111111101
print(hammingWeight(n))
