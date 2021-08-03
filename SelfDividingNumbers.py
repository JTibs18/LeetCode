# A self-dividing number is a number that is divisible by every digit it contains.
# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# A self-dividing number is not allowed to contain the digit zero.
# Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].

def selfDividingNumbers(left, right):
    ans = []

    for num in range(left, right + 1):
        selfDiv = True
        for digit in str(num):
            if int(digit) == 0 or int(num) % int(digit) != 0:
                selfDiv = False
                break
        if selfDiv == True:
            ans.append(num)
    return ans

#Test cases
left = 1
right = 22
print(selfDividingNumbers(left, right))

left = 47
right = 85
print(selfDividingNumbers(left, right))
