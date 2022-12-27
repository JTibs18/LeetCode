# You are given a positive integer num consisting only of digits 6 and 9.
# Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

def maximum69Number(num): 
    num = str(num)
    
    for indx, n in enumerate(num): 
        if n == "6":
            num = num[:indx] + "9" + num[indx + 1:] 
            break 
    
    return int(num)

# Test cases 
num = 9669
print(maximum69Number(num))

num = 9996
print(maximum69Number(num))

num = 9999
print(maximum69Number(num))
