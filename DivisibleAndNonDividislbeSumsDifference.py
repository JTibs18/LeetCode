# You are given positive integers n and m.
# Define two integers, num1 and num2, as follows:
#   num1: The sum of all integers in the range [1, n] that are not divisible by m.
#   num2: The sum of all integers in the range [1, n] that are divisible by m.
# Return the integer num1 - num2.

def differenceOfSums(n, m):
    nSum = 0
    mSum = 0 

    for i in range(1, n + 1):
        if i % m != 0:
            nSum += i 
    
    for i in range(1, n + 1):
        if i % m == 0:
            mSum += i 

    return nSum - mSum 

# Test cases
n = 10
m = 3
print(differenceOfSums(n, m))

n = 5
m = 6
print(differenceOfSums(n, m))

n = 5
m = 1
print(differenceOfSums(n, m))
