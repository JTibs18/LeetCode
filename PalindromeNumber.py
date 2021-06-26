# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is palindrome while 123 is not.

#converting int to str method
def isPalindrome(x):
    strX = str(x)
    revX = strX[::-1]
    return (strX == revX)

#int is not converted to string
def isPalindrome2(x):
    checkNum = abs(x)
    newNum = 0

    def helperFun(x, newNum):
        if x < 10:
            newNum = (newNum * 10) + x
            return newNum
        else:
            newNum = (newNum * 10) + (x % 10)
            return helperFun(x // 10, newNum)

    return helperFun(checkNum, newNum) == x

#Test cases
x = 121
print(isPalindrome(x))
print(isPalindrome2(x))

x = -121
print(isPalindrome(x))
print(isPalindrome2(x))

x = 10
print(isPalindrome(x))
print(isPalindrome2(x))

x = -101
print(isPalindrome(x))
print(isPalindrome2(x))
