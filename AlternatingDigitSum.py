# For Weekly Contest #329 Question #1
# You are given a positive integer n. Each digit of n has a sign according to the following rules:
# The most significant digit is assigned a positive sign.
# Each other digit has an opposite sign to its adjacent digits.
# Return the sum of all digits with their corresponding sign.

def alternateDigitSum(n): 
    addition = True 
    sum = 0 
    n = str(n)

    for i in n: 
        if addition == True: 
            sum += int(i) 
            addition = False
        else: 
            sum -= int(i) 
            addition = True 
    
    return sum

# Test cases
n = 521
print(alternateDigitSum(n))

n = 111
print(alternateDigitSum(n))

n = 886996
print(alternateDigitSum(n))
