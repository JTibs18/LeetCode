# There is an integer array nums that consists of n unique elements, but you have forgotten it. However, you do remember every pair of adjacent elements in nums.
# You are given a 2D integer array adjacentPairs of size n - 1 where each adjacentPairs[i] = [ui, vi] indicates that the elements ui and vi are adjacent in nums.
# It is guaranteed that every adjacent pair of elements nums[i] and nums[i+1] will exist in adjacentPairs, either as [nums[i], nums[i+1]] or [nums[i+1], nums[i]]. The pairs can appear in any order.
# Return the original array nums. If there are multiple solutions, return any of them.

from collections import defaultdict

def restoreArray(adjacentPairs): 
    pairs = defaultdict(set)
    restoredArray = []

    for u, v in adjacentPairs: 
        pairs[u].add(v)
        pairs[v].add(u)

    for key, val in pairs.items():
        if len(val) == 1: 
            curNode = key 
            restoredArray.append(key)
            break 

    while pairs[curNode]: 
        newNode = pairs[curNode].pop()
        restoredArray.append(newNode)
        pairs[newNode].remove(curNode)
        curNode = newNode
    
    return restoredArray
    
# Test cases
adjacentPairs = [[2, 1], [3, 4], [3, 2]]
print(restoreArray(adjacentPairs))

adjacentPairs = [[4, -2], [1, 4], [-3, 1]]
print(restoreArray(adjacentPairs))

adjacentPairs = [[100000, -100000]]
print(restoreArray(adjacentPairs))
