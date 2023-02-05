# For Weekly Contest 331 Question #1

# You are given an integer array gifts denoting the number of gifts in various piles. Every second, you do the following
# Choose the pile with the maximum number of gifts.
# If there is more than one pile with the maximum number of gifts, choose any.
# Leave behind the floor of the square root of the number of gifts in the pile. Take the rest of the gifts.
# Return the number of gifts remaining after k seconds.

import heapq
import math 

def pickGifts(gifts, k): 
    gifts = [-gift for gift in gifts]
    heapq.heapify(gifts)

    while k: 
        largest = heapq.heappop(gifts)
        heapq.heappush(gifts, (-1 * math.floor(math.sqrt(-1 * largest))))
        k -= 1 

    return -1 * sum(gifts)

# Test cases 
gifts = [25,64,9,4,100]
k = 4
print(pickGifts(gifts, k))

gifts = [1,1,1,1] 
k = 4
print(pickGifts(gifts, k))
