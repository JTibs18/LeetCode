# The array-form of an integer num is an array representing its digits in left to right order.
# For example, for num = 1321, the array form is [1,3,2,1].
# Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.

import math 

def addToArrayForm(num, k): 
    k = str(k)
    indx = len(k) - 1
    carryOver = 0 
    result = []

    for i, _ in enumerate(num): 
        if indx < 0: 
            curSum = num[len(num) - 1 - i] + carryOver
        else:  
            curSum = num[len(num) - 1 - i] + int(k[indx]) + carryOver
        
        if curSum > 9: 
            carryOver = math.floor(curSum / 10)
        else: 
            carryOver = 0

        result.append(curSum % 10)
        indx -= 1
    
    if indx >= 0: 
        for i in range(indx + 1): 
            curSum = int(k[indx - i]) + carryOver

            if curSum > 9: 
                carryOver = math.floor(curSum / 10)
            else: 
                carryOver = 0

            result.append(curSum % 10)

    if carryOver != 0: 
        result.append(carryOver)

    result.reverse()
    return result

#  Test cases 
num = [1,2,0,0]
k = 34
print(addToArrayForm(num, k))

num = [2,7,4]
k = 181
print(addToArrayForm(num, k))

num = [2,1,5]
k = 806
print(addToArrayForm(num, k))

num = [0]
k = 23
print(addToArrayForm(num, k))

num = [0]
k = 10000
print(addToArrayForm(num, k))

num = [6]
k = 809
print(addToArrayForm(num, k))

num = [7]
k = 993
print(addToArrayForm(num, k))
