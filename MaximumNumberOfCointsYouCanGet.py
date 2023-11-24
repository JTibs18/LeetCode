# There are 3n piles of coins of varying size, you and your friends will take piles of coins as follows:
#   In each step, you will choose any 3 piles of coins (not necessarily consecutive).
#   Of your choice, Alice will pick the pile with the maximum number of coins.
#   You will pick the next pile with the maximum number of coins.
#   Your friend Bob will pick the last pile.
#   Repeat until there are no more piles of coins.
# Given an array of integers piles where piles[i] is the number of coins in the ith pile.
# Return the maximum number of coins that you can have.

def maxCoins(piles):
    piles.sort(reverse=True)
    myPileCount = 0 
    ptr1 = 1 
    ptr2 = len(piles) - 1 

    while ptr1 < ptr2: 
        myPileCount += piles[ptr1]
        ptr1 += 2 
        ptr2 -= 1 
    
    return myPileCount

# Test cases
piles = [2,4,1,2,7,8]
print(maxCoins(piles))

piles = [2,4,5]
print(maxCoins(piles))

piles = [9,8,7,6,5,1,2,3,4]
print(maxCoins(piles))
