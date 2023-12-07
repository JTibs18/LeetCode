# Alice and Bob play a game with piles of stones. There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].
# The objective of the game is to end with the most stones. The total number of stones across all the piles is odd, so there are no ties.
# Alice and Bob take turns, with Alice starting first. Each turn, a player takes the entire pile of stones either from the beginning or from the end of the row. This continues until there are no more piles left, at which point the person with the most stones wins.
# Assuming Alice and Bob play optimally, return true if Alice wins the game, or false if Bob wins.

def stoneGame(piles):
    score = 0
    AliceTurn = True 

    while piles: 
        if piles[0] > piles[-1] or (piles[0] == piles[-1] and len(piles) > 2 and piles[1] > piles[-2]):
            if AliceTurn:
                score += piles.pop(0)
            else:
                score -= piles.pop()
        elif piles[0] < piles[-1] or (piles[0] == piles[-1] and len(piles) > 2 and piles[1] < piles[-2]):
            if AliceTurn:
                score += piles.pop()
            else:
                score -= piles.pop(0)
        else:
            if AliceTurn:
                score += piles.pop()
            else:
                score -= piles.pop()

    if score > 0:
        return True 

# Test cases
piles = [5, 3, 4, 5]
print(stoneGame(piles))

piles = [3, 7, 2, 3]
print(stoneGame(piles))
