# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

def checkStraightLine(coordinates):
    x = False
    for indx, coord in enumerate(coordinates):
        if indx == 0:
            ogX = coord[0]
            ogY = coord[1]
        elif indx == 1:
            diffX = coord[0] - ogX
            diffY = coord[1] - ogY
            if diffX == 0:
                diff = ogX
                x = True
            else:
                diff = diffY / diffX
        else:
            dX = coord[0] - ogX
            dY = coord[1] - ogY
            if x == True:
                newDiff = coord[0]
            elif dX == 0:
                return False
            else:
                newDiff = dY / dX

            if newDiff != diff:
                return False
    return True

#Test case
coordinates = [[1,2], [2,3], [3, 4], [4,5], [5, 6], [6,7]]
print(checkStraightLine(coordinates))

coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
print(checkStraightLine(coordinates))

coordinates = [[0,0],[0,1],[0,-1]]
print(checkStraightLine(coordinates))

coordinates = [[2,1],[4,2],[6,3]]
print(checkStraightLine(coordinates))

coordinates = [[1,1],[2,2],[2,0]]
print(checkStraightLine(coordinates))

coordinates = [[1,-8],[2,-3],[1,2]]
print(checkStraightLine(coordinates))

coordinates = [[2,4],[2,5],[2,8]]
print(checkStraightLine(coordinates))

coordinates = [[0,0],[0,5],[5,0],[1337,0],[0,1337]]
print(checkStraightLine(coordinates))

coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[1,8]]
print(checkStraightLine(coordinates))
