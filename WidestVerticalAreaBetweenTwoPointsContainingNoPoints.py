# Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area between two points such that no points are inside the area.
# A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The widest vertical area is the one with the maximum width.
# Note that points on the edge of a vertical area are not considered included in the area.

def maxWidthOfVerticalArea(points):
    points.sort()
    diff = 0

    for indx in range(len(points) - 2):
        if points[indx + 1][0] - points[indx][0] > diff:
            diff = points[indx + 1][0] - points[indx][0]
    
    return diff

# Test cases
points = [[8,7],[9,9],[7,4],[9,7]]
print(maxWidthOfVerticalArea(points))

points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
print(maxWidthOfVerticalArea(points))
