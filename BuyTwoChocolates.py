# You are given an integer array prices representing the prices of various chocolates in a store. You are also given a single integer money, which represents your initial amount of money.
# You must buy exactly two chocolates in such a way that you still have some non-negative leftover money. You would like to minimize the sum of the prices of the two chocolates you buy.
# Return the amount of money you will have leftover after buying the two chocolates. If there is no way for you to buy two chocolates without ending up in debt, return money. Note that the leftover must be non-negative.

def buyChoco(prices, money):
    prices.sort()

    if prices[0] + prices[1] <= money:
        return money - (prices[0] + prices[1]) 

    return money

# Test cases
prices = [1,2,2]
money = 3
print(buyChoco(prices, money))

prices = [3,2,3]
money = 3
print(buyChoco(prices, money))

prices = [98,54,6,34,66,63,52,39]
money = 62
print(buyChoco(prices, money))
