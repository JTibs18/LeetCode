# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).

def fib(n):
    if n == 0:
        return 0
    elif n < 3:
        return 1

    solved = [1, 1]

    for num in range(2, n):
        solved.append(solved[num - 1] + solved[num - 2])
    return solved[len(solved) - 1]

#Test Cases
n = 2
print(fib(n))

n = 3
print(fib(n))

n = 4
print(fib(n))
