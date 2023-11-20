# You are given an integer array prices where prices[i] is the price of the ith item in a shop.
# There is a special discount for items in the shop. If you buy the ith item, then you will receive a discount equivalent to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i]. Otherwise, you will not receive any discount at all.
# Return an integer array answer where answer[i] is the final price you will pay for the ith item of the shop, considering the special discount.

def finalPrices(prices):
    stack = []
    answer = []

    for i in range(len(prices) - 1, -1, -1):
        while len(stack) and stack[-1] > prices[i]:
            stack.pop()
        
        if len(stack) == 0:
            answer.append(prices[i])
        else: 
            answer.append(prices[i] - stack[-1])
        
        stack.append(prices[i])

    answer.reverse()
    return answer

# Test cases
prices = [8, 4, 6, 2, 3]
print(finalPrices(prices))

prices = [1, 2, 3, 4, 5]
print(finalPrices(prices))

prices = [10, 1, 1, 6]
print(finalPrices(prices))

prices = [8,7,4,2,8,1,7,7,10,1]
print(finalPrices(prices))

prices = [4,7,1,9,4,8,8,9,4]
print(finalPrices(prices))
