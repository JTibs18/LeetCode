# You are given a string num representing a large integer. An integer is good if it meets the following conditions:
#   It is a substring of num with length 3.
#   It consists of only one unique digit.
# Return the maximum good integer as a string or an empty string "" if no such integer exists.
# Note:
#   A substring is a contiguous sequence of characters within a string.
#   There may be leading zeroes in num or a good integer.

def largestGoodInteger(num):
    largestGoodNum = ''

    for i in range(0, len(num) - 2):
        if num[i] == num[i + 1] and num[i + 1] == num[i + 2] and (largestGoodNum == "" or num[i] > largestGoodNum[0]): 
            largestGoodNum = num[i] * 3
    
    return largestGoodNum

# Test cases
num = "6777133339"
print(largestGoodInteger(num))

num = "2300019"
print(largestGoodInteger(num))

num = "42352338"
print(largestGoodInteger(num))
