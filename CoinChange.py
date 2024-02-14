# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
# You may assume that you have an infinite number of each kind of coin.

def coinChange(coins, amount):
    def helper(amount, memo = {}):
        if amount in memo:
            return memo[amount]
        
        if not amount:
            return 0
        
        if amount < 0:
            return None
        
        shortestCombination = float("inf")
        
        for i in coins:
            remainderCount = helper(amount - i) 
            if remainderCount != None and remainderCount + 1 < shortestCombination:
                shortestCombination = remainderCount + 1

        memo[amount] = shortestCombination
        return shortestCombination

    changeCount = helper(amount)

    if changeCount == float("inf"):
        return -1
    return changeCount

# Test cases
coins = [1, 2, 5]
amount = 11
print(coinChange(coins, amount))

coins = [2]
amount = 3
print(coinChange(coins, amount))

coins = [1]
amount = 0
print(coinChange(coins, amount))