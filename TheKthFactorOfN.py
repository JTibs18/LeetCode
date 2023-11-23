# You are given two positive integers n and k. A factor of an integer n is defined as an integer i where n % i == 0.
# Consider a list of all factors of n sorted in ascending order, return the kth factor in this list or return -1 if n has less than k factors.

def kthFactor(n, k):
    i = 0
    
    while k: 
        i += 1 

        if i > n: 
            return -1 
        elif n % i == 0:
            k -= 1 
        
    return i

# Test cases
n = 12
k = 3
print(kthFactor(n, k))

n = 7
k = 2
print(kthFactor(n, k))

n = 4
k = 4
print(kthFactor(n, k))
