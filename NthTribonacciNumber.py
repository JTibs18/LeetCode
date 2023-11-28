# The Tribonacci sequence Tn is defined as follows: 
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
# Given n, return the value of Tn.

# slower runtime, same memory 
def tribonacci1 (n: int):
    fibonacciSequence = [0, 1, 1]

    for i in range(n - 2):
        fibonacciSequence.append(sum(fibonacciSequence[i:i+3]))
    
    return fibonacciSequence[n]  

# faster runtime, same memory 
def tribonacci(n):
    fibonacciSequence = [0, 1, 1]
    tribSum = 2

    for i in range(n - 2):
        fibonacciSequence.append(tribSum)
        tribSum += (-1 * fibonacciSequence[i]) + fibonacciSequence[i + 3]
    
    return fibonacciSequence[n]  

# Test cases
n = 4
print(tribonacci(n))

n = 25
print(tribonacci(n))

n = 0
print(tribonacci(n))
