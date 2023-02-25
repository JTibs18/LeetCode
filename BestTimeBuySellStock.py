# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

def maxProfit(prices): 
    cheapestPrice = 100000
    profit = 0 

    for i in prices: 
        if i < cheapestPrice: 
            cheapestPrice = i 
        elif i - cheapestPrice > profit: 
            profit = i - cheapestPrice
        
    return profit 

#Test cases
prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))

prices = [7, 6, 4, 3, 1]
print(maxProfit(prices))

prices = [1, 2]
print(maxProfit(prices))

prices = [1,4,2]
print(maxProfit(prices))

prices = [2,4,1]
print(maxProfit(prices))

prices = [1,2,4]
print(maxProfit(prices))

prices = [3,2,6,5,0,3]
print(maxProfit(prices))

prices = [2,7,1,4]
print(maxProfit(prices))
