# Given two positive integers a and b, return the number of common factors of a and b.
# An integer x is a common factor of a and b if x divides both a and b.

def commonFactors(a, b):
    commonFactorCount = 0 

    for i in range(1, min(a, b) + 1): 
        if a % i == 0 and b % i == 0: 
            commonFactorCount += 1
    
    return commonFactorCount

# Test cases
a = 12
b = 6
print(commonFactors(a, b))

a = 25
b = 30 
print(commonFactors(a, b))
