# You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank.
# Return the wealth that the richest customer has.
# A customer's wealth is the amount of money they have in all their bank accounts.
# The richest customer is the customer that has the maximum wealth.

def maximumWealth(accounts):
    maxSum = 0
    for indx, value in enumerate(accounts):
        if sum(value) > maxSum:
            maxSum = sum(value)
    return maxSum 

#Test cases
accounts = [[1, 2, 3], [3, 2, 1]]
print(maximumWealth(accounts))

accounts = [[1, 5], [7, 3], [3, 5]]
print(maximumWealth(accounts))

accounts = [[2,8,7],[7,1,3],[1,9,5]]
print(maximumWealth(accounts))
