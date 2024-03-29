# Write an algorithm to determine if a number n is happy.
# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

def isHappy(n):
    allNums = set() 

    while n not in allNums:
        digits = [int(x) for x in str(n)]
        allNums.add(n)
        n = 0
        
        for i in digits: 
            n += i ** 2 
        
        if n == 1: 
            return True 
    
    return False 

# Test cases
n = 19 
print(isHappy(n))

n = 2 
print(isHappy(n))

n = 3 
print(isHappy(n))
