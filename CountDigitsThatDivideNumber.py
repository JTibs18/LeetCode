# Given an integer num, return the number of digits in num that divide num.
# An integer val divides nums if nums % val == 0.

# first attempt 
def countDigits1(num): 
    digits = dict()
    count = 0 

    for i in str(num): 
        if int(i) in digits: 
            digits[int(i)] += 1 
        else: 
            digits[int(i)] = 1 

    for key, value in digits.items(): 
        if num % key == 0: 
            count += 1 * value

    return count

# faster solution and uses less memory
def countDigits(num): 
    count = 0 

    for i in str(num): 
        if num % int(i) == 0: 
            count += 1 

    return count

# Test cases
num = 7
print(countDigits(num))

num = 121
print(countDigits(num))

num = 1248
print(countDigits(num))
