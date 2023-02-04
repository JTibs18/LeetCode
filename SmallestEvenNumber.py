# Given a positive integer n, return the smallest positive integer that is a multiple of both 2 and n.

def smallestEvenMultiple(n): 
    if n % 2 == 0: 
        return n 
    else: 
        return n * 2

# Test cases
n = 5
print(smallestEvenMultiple(n))

n = 6
print(smallestEvenMultiple(n))