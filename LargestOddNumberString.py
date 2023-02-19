# You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.
# A substring is a contiguous sequence of characters within a string.

# Faster solution but uses more memory 
def largestOddNumber(num):
    while num: 
        if int(num[len(num) - 1]) % 2 != 0: 
            return num
        num = num[:-1]
    return ""

# Slower solution but uses less memory
def largestOddNumber2(num):
    for i in range(len(num) - 1, -1, -1):
        if int(num[i]) % 2 != 0: 
            return num
        num = num[:-1]
    return ""

# Test cases 
num = "52"
print(largestOddNumber(num))

num = "4206"
print(largestOddNumber(num))

num = '35427'
print(largestOddNumber(num))
