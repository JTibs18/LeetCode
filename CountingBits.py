# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

def countBits(n): 
    bitCount = []

    for i in range(n + 1):
        if i == 0:
            bitCount.append(0)
        elif i == 1:
            bitCount.append(1)
        elif i % 2 == 0: 
            bitCount.append(bitCount[i // 2])
        else:
            bitCount.append(bitCount[(i // 2)] + 1)

    return bitCount

# Test cases
n = 2
print(countBits(n))

n = 5
print(countBits(n))

n = 8
print(countBits(n))
