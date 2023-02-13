# Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

import math 

def countOdds(low, high): 
    diff = (high + 1) - low 
    if high % 2 == 0:
        return math.floor(diff / 2)
    return math.ceil(diff / 2)

# Test cases
low = 3
high = 7
print(countOdds(low, high))

low = 8
high = 10
print(countOdds(low, high))

low = 976487647
high = 989817026
print(countOdds(low, high))