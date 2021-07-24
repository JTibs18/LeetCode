# Given an integer n, add a dot (".") as the thousands separator and return it in string format.

def thousandSeparator(n):
    num = ""

    if len(str(n)) < 4:
        return str(n)

    for count, dig in enumerate(reversed(str(n))):
        num = dig + num
        if (count + 1) % 3 == 0 and count + 1 != len(str(n)):
            num =  "." + num
    return num

#Test Cases
n = 987
print(thousandSeparator(n))

n = 1234
print(thousandSeparator(n))

n = 123456789
print(thousandSeparator(n))

n = 0
print(thousandSeparator(n))
