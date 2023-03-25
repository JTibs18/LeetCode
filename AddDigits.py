# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

# naive approach, better memory 
def addDigits1(num):
    while (len(str(num)) > 1): 
        num = sum([int(x) for x in str(num)])
    
    return num

# takes up more memory, O(1) runtime inspired by https://leetcode.com/problems/add-digits/solutions/1754049/easy-o-1-explanation-with-example/
def addDigits(num):
    if num == 0:  
        return 0
    if num % 9 == 0:
        return 9
    return num % 9 

# Test cases
num = 38 
print(addDigits(num))

num = 0 
print(addDigits(num))
