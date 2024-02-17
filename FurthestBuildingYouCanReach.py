# You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.
# You start your journey from building 0 and move to the next building by possibly using bricks or ladders.
# While moving from building i to building i+1 (0-indexed),
#   If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
#   If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.
# Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.

import heapq

# TLE
def furthestBuilding(heights, bricks, ladders):
        usedBricks = []
        ptr = 0 

        while ptr < len(heights) - 1: 
            if heights[ptr] < heights[ptr + 1]:
                neededBricks = heights[ptr + 1] - heights[ptr] 

                bricks -= neededBricks
                usedBricks.append(neededBricks)

                if bricks < 0 and ladders > 0:
                    ladders -= 1 
                    addBricksBack = max(usedBricks)
                    bricks += addBricksBack
                    usedBricks.remove(addBricksBack)
                elif bricks < 0 and ladders == 0:
                    break
            
            ptr += 1

        return ptr

# optimal solution with heap
def furthestBuilding(heights, bricks, ladders):
    usedBricks = []
    ptr = 0 

    while ptr < len(heights) - 1: 
        if heights[ptr] < heights[ptr + 1]:
            neededBricks = heights[ptr + 1] - heights[ptr] 

            bricks -= neededBricks
            heapq.heappush(usedBricks, -1 * neededBricks)

            if bricks < 0 and ladders > 0:
                ladders -= 1 
                bricks += -1 * heapq.heappop(usedBricks)
            elif bricks < 0 and ladders == 0:
                break
        
        ptr += 1

    return ptr

# Test cases
heights = [4,2,7,6,9,14,12]
bricks = 5
ladders = 1
print(furthestBuilding(heights, bricks, ladders))

heights = [4,12,2,7,3,18,20,3,19]
bricks = 10
ladders = 2
print(furthestBuilding(heights, bricks, ladders))

heights = [14,3,19,3]
bricks = 17
ladders = 0
print(furthestBuilding(heights, bricks, ladders))

heights = [1, 2, 4, 7]
bricks = 3
ladders = 1
print(furthestBuilding(heights, bricks, ladders))
