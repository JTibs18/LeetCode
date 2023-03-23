# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.
# Beats 90% in runtime and memory

def plusOne(digits): 
    lastDigit = len(digits) - 1 

    while digits[lastDigit] == 9: 
        if lastDigit == 0: 
            digits[lastDigit] = 1
            digits.append(-1)
        else: 
            digits[lastDigit] = 0

        lastDigit -= 1 

    digits[lastDigit] += 1 
    return digits 

# Test cases
digits = [1,2,3]
print(plusOne(digits))

digits = [4,3,2,1]
print(plusOne(digits))

digits = [9]
print(plusOne(digits))
