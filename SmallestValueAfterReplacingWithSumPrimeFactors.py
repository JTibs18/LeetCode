# For weekly contest #324 Question #2

# You are given a positive integer n.
# Continuously replace n with the sum of its prime factors.
# Note that if a prime factor divides n multiple times, it should be included in the sum as many times as it divides n.
# Return the smallest value n will take on.

def smallestValue(n):
    previous = 0
    
    while previous != n: 
        primes = 0
        previous = n
        c = 2
        
        while(n > 1):
            if(n % c == 0):
                primes += c
                n = n / c
            else:
                c = c + 1

        n = primes 
    return primes

# Test cases
n = 15
print(smallestValue(n))

n = 3
print(smallestValue(n))
