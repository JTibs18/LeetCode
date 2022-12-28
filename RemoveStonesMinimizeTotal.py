# You are given a 0-indexed integer array piles, where piles[i] represents the number of stones in the ith pile, and an integer k. You should apply the following operation exactly k times:
# Choose any piles[i] and remove floor(piles[i] / 2) stones from it.
# Notice that you can apply the operation on the same pile more than once.
# Return the minimum possible total number of stones remaining after applying the k operations.
# floor(x) is the greatest integer that is smaller than or equal to x (i.e., rounds x down).

import heapq

def minStoneSum(piles, k):
    piles = [-pile for pile in piles]
    heapq.heapify(piles)

    while k:
        curPile = heapq.heappop(piles)
        curPile = curPile // 2 
        heapq.heappush(piles, curPile)
        k -= 1 
    return -sum(piles)

#Test cases
piles = [5,4,9]
k = 2
print(minStoneSum(piles, k))

piles = [4,3,6,7]
k = 3
print(minStoneSum(piles, k))

# Note about heaps: the smallest element is at the top of heap.
# So to get the maximum number of all positive numbers from a heap, 
# convert to negative numbers so largest positive becomes smallest negative and is thus at the top of heap. 

# Notice that instead of using for i in range(k) to iterate k times, 
# use while k and decrement k until k = 0, which is false and will break the while loop! 

# Helpful source: https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/