# It is a sweltering summer day, and a boy wants to buy some ice cream bars.
# At the store, there are n ice cream bars. You are given an array costs of length n, where costs[i] is the price of the ith ice cream bar in coins. The boy initially has coins coins to spend, and he wants to buy as many ice cream bars as possible. 
# Return the maximum number of ice cream bars the boy can buy with coins coins.
# Note: The boy can buy the ice cream bars in any order.

def maxIceCream(costs, coins): 
    costs = sorted(costs)
    spentCoins = 0 
    curCost = 0 

    for i in costs: 
        if i + curCost <= coins: 
            curCost += i
            spentCoins += 1 
        else:
            break
    
    return spentCoins

# Test cases 
costs = [1, 3, 2, 4, 1]
coins = 7
print(maxIceCream(costs, coins))

costs = [10,6,8,7,7,8]
coins = 5
print(maxIceCream(costs, coins))

costs = [1,6,3,1,2,5]
coins = 20
print(maxIceCream(costs, coins))

costs = [7,3,3,6,6,6,10,5,9,2]
coins = 56
print(maxIceCream(costs, coins))
