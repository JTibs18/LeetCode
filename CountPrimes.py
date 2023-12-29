# Given an integer n, return the number of prime numbers that are strictly less than n.
# With help from https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

import math

# naive approach, will result in TLE
def countPrimes1(n):
    count = 0
    isPrime = False

    for i in range(2, n):
        for x in range(2, (i // 2) + 1):
            if i % x == 0:
                isPrime = True
                break 

        if not isPrime:
            count += 1 
        else:
            isPrime = False 

    return count        

# okay solution: attempting to count numbers that are not prime, then subtracting from all numbers to get prime numbers 
def countPrimes2(n):
    foundPrimes = set()

    if n < 3: 
        return 0

    for i in range(2, round(math.sqrt(n)) + 1):
        if i not in foundPrimes:
            for j in range(1, 5):
                for x in range(i ** 2, n, j * i):
                    foundPrimes.add(x)

    return n - len(foundPrimes) - 2

# best solution: using Sieve of Eratosthenes 
def countPrimes(n):
    nums = [True for _ in range(n - 2)]

    if n < 3:
        return 0
    
    for i in range(2, round(math.sqrt(n)) + 1):
        if nums[i - 2] == True:
            for j in range(1, 5):
                for x in range(i ** 2, n, j * i):
                    nums[x - 2] = False
    
    return len([x for x in nums if x == True])

# Test cases
n = 10
print(countPrimes(n))

n = 0
print(countPrimes(n))

n = 1 
print(countPrimes(n))

n = 2
print(countPrimes(n))

n = 3
print(countPrimes(n))
