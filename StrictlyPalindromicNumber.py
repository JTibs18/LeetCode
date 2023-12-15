# An integer n is strictly palindromic if, for every base b between 2 and n - 2 (inclusive), the string representation of the integer n in base b is palindromic.
# Given an integer n, return true if n is strictly palindromic and false otherwise.
# A string is palindromic if it reads the same forward and backward.
# Help with converting a number to any base: https://stackoverflow.com/questions/2267362/how-to-convert-an-integer-to-a-string-in-any-base

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

def isStrictlyPalindromic(n):
    for b in range(2, n - 1):
        based = str(numberToBase(n, b))
        ptr1 = 0
        ptr2 = len(based) - 1

        while ptr1 < ptr2:
            if based[ptr1] != based[ptr2]: 
                return False 

            ptr1 += 1
            ptr2 -= 1 

    return True

# Test cases
n = 9
print(isStrictlyPalindromic(n))

n = 4
print(isStrictlyPalindromic(n))
