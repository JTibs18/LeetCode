# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
# Return the minimum integer k such that she can eat all the bananas within h hours.

import math

def minEatingSpeed(piles, h): 
    leftPtr = 1
    rightPtr = max(piles)
    answer = 0 

    while leftPtr <= rightPtr: 
        midPtr = (leftPtr + rightPtr) // 2 
        k = 0 

        for i in piles: 
            if i < midPtr: 
                k += 1
            else: 
                k += math.ceil(i / midPtr)

        if k > h: 
            leftPtr = midPtr + 1 
        else:
            rightPtr = midPtr
            if answer == midPtr: 
                break 
            answer = midPtr
            
    return answer

# Test cases
piles = [3,6,7,11]
h = 8
print(minEatingSpeed(piles, h))

piles = [30,11,23,4,20]
h = 5
print(minEatingSpeed(piles, h))

piles = [30,11,23,4,20]
h = 6
print(minEatingSpeed(piles, h))

piles = [312884470]
h = 312884469
print(minEatingSpeed(piles, h))

piles = [1,1,1,999999999]
h = 10
print(minEatingSpeed(piles, h))
