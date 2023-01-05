# There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.
# Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.
# Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

def findMinArrowShots(points): 
    points = sorted(points)
    newIntervals = []
    newIntervals.append(points[0])

    for i in points[1:]: 
        if newIntervals[-1][0] <= i[0] and i[0] <= newIntervals[-1][-1]: 
            newIntervals[-1][-1] = min(newIntervals[-1][-1], i[-1])
        else: 
            newIntervals.append(i)

    return len(newIntervals)

# Test cases
points = [[10,16],[2,8],[1,6],[7,12]]
print(findMinArrowShots(points))

points = [[1,2],[3,4],[5,6],[7,8]]
print(findMinArrowShots(points))

points = [[1,2],[2,3],[3,4],[4,5]]
print(findMinArrowShots(points))
