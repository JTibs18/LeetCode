# You are given a strictly increasing integer array rungs that represents the height of rungs on a ladder. You are currently on the floor at height 0, and you want to reach the last rung.
# You are also given an integer dist. You can only climb to the next highest rung if the distance between where you are currently at (the floor or on a rung) and the next rung is at most dist. You are able to insert rungs at any positive integer height if a rung is not already there.
# Return the minimum number of rungs that must be added to the ladder in order for you to climb to the last rung.
import math

def minNumberRungs(rungs, dist):
    needed = 0

    if rungs[0] > dist:
        if dist == 1:
            needed += math.ceil(rungs[0] / dist) - 1
        else:
            needed += math.ceil(rungs[0] / dist) - 1

    for num in range(1, len(rungs)):
        if rungs[num] - rungs[num - 1] > dist:
            if dist == 1:
                needed += math.ceil((rungs[num] - rungs[num - 1]) / dist) - 1
            else:
                needed += math.ceil((rungs[num] - rungs[num - 1]) / dist) - 1
    return needed

#Test cases
rungs = [1,3,5,10]
dist = 2
print(minNumberRungs(rungs, dist))

rungs = [3,6,8,10]
dist = 3
print(minNumberRungs(rungs, dist))

rungs = [3,4,6,7]
dist = 2
print(minNumberRungs(rungs, dist))

rungs = [5]
dist = 10
print(minNumberRungs(rungs, dist))

rungs = [3]
dist = 1
print(minNumberRungs(rungs, dist))

rungs = [12, 24]
dist = 4
print(minNumberRungs(rungs, dist))
