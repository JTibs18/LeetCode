# The k-beauty of an integer num is defined as the number of substrings of num when it is read as a string that meet the following conditions:
#    It has a length of k.
#   It is a divisor of num.
# Given integers num and k, return the k-beauty of num.
# Note:
#   Leading zeros are allowed.
#   0 is not a divisor of any value.
# A substring is a contiguous sequence of characters in a string.

def divisorSubstrings(num, k):
    ptr1 = 0
    count = 0
    strNum = str(num)

    while ptr1 + k < len(strNum) + 1:
        if int(strNum[ptr1: ptr1 + k]) and not (num % int(strNum[ptr1:ptr1 + k])):
            count += 1 
        
        ptr1 += 1 

    return count

# Test cases
num = 240
k = 2
print(divisorSubstrings(num, k))

num = 430043
k = 2
print(divisorSubstrings(num, k))
