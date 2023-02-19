# Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.
# He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.
# Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.

def totalMoney(n): 
    mondayAmount = 0
    curAmount = 0
    total = 0 

    for i in range(n): 
        if i % 7 == 0: 
            mondayAmount += 1 
            curAmount = mondayAmount 
        else: 
            curAmount += 1 
        total += curAmount 
    
    return total

# Test cases
n = 4
print(totalMoney(n))

n = 10
print(totalMoney(n))

n = 20
print(totalMoney(n))
