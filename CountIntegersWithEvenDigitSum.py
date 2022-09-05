# Given a positive integer num, return the number of positive integers less than or equal to num whose digit sums are even.
# The digit sum of a positive integer is the sum of all its digits.

# For weekly contest 281. Accepted

import math

def countEven(num):
    ogNum = num

    if num > 9:
        num = str(num)
        sum = 0
        for i in num:
            sum += int(i)
        sum = int(sum)
    else:
        sum = num
    if sum % 2 == 0:
        return math.floor(ogNum / 2)
    else:
        return math.ceil(ogNum / 2) - 1

#Test cases
num = 4
print(countEven(num))

num = 30
print(countEven(num))

num = 13
print(countEven(num))
